import requests
from bs4 import BeautifulSoup


def get_prices(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html5lib')
    name = soup.find('span', attrs={'class': 'B_NuCI'}).get_text()
    price = soup.find('div', attrs={'class': '_30jeq3 _16Jk6d'}).get_text()
    return name, price


if __name__ == '__main__':
    URL_list = [
        "https://www.flipkart.com/yumin-mobile-holder-pouch-bag-activa-jupiter-pleasure-all-scooter-scooty-7-inches-bike/p/itm4f1131e77c7d8?pid=BMHGAKFDZVSSQS22&lid=LSTBMHGAKFDZVSSQS22NMJ6QN&marketplace=FLIPKART&store=1mt&srno=b_1_6&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_4.dealCard.OMU_O496H87A7BR7_3&otracker1=hp_omu_SECTIONED_manualRanking_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_3&fm=neo%2Fmerchandising&iid=en_Ws8QRa3fIChYcnYWYROUwoL7MJlpYmrPtROlboWbyaMZObWZ7Uljqv8CunEFq65p0a3c2DrZPQLHlNbeU%2BxQAg%3D%3D&ppt=hp&ppn=homepage&ssid=xyr6or5qxc0000001645500402414",
        "https://www.flipkart.com/realme-8i-space-black-64-gb/p/itm7ab6edcb3b2a4?pid=MOBG63YXSVKZ5AZJ&lid=LSTMOBG63YXSVKZ5AZJOKGHIO&marketplace=FLIPKART&fm=personalisedRecommendation%2Fp2p-same&iid=R%3As%3Bp%3AMOBG24GTKAAJZZHY%3Bpt%3Ahp%3Buid%3Ac3693190-938f-11ec-bec0-05e1cd695263%3B.MOBG63YXSVKZ5AZJ&ppt=browse&ppn=browse&otracker=hp_reco_Suggested%2BItems_3_13.productCard.PMU_V2_realme%2B8i%2B%2528Space%2BBlack%252C%2B64%2BGB%2529_MOBG63YXSVKZ5AZJ_personalisedRecommendation%2Fp2p-same_2&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2Fp2p-same_Suggested%2BItems_DESKTOP_HORIZONTAL_productCard_cc_3_NA_view-all&cid=MOBG63YXSVKZ5AZJ",
        "https://www.flipkart.com/samsung-crystal-4k-138-cm-55-inch-ultra-hd-4k-led-smart-tv/p/itm3d8f2879a7625?pid=TVSG2CG7HAVAZTXF&lid=LSTTVSG2CG7HAVAZTXFEAA8L0&marketplace=FLIPKART&store=ckf%2Fczl&srno=b_1_2&otracker=hp_reco_Shop%2BFor%2BTVs_1_18.dealCard.OMU_cid%3AS_F_NWF_PC6a082af02f38ad_b___NONE_ALL%3Bnid%3Ackf_czl_%3Bet%3APC%3Beid%3APC6a082af02f38ad%3Bmp%3AF%3Bct%3Ab%3B_9&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2FintentPivoted_Shop%2BFor%2BTVs_DESKTOP_HORIZONTAL_dealCard_cc_1_NA_view-all_9&fm=personalisedRecommendation%2FintentPivoted&iid=en_RQ%2B%2BFbZKA4NgqpST%2FH6KwCwYPTEh35zRXhxIYTGqcIaE%2FTSOJnJzFXn1WCj5g3N7rBCWo1k92ww5pP3IwJl9MA%3D%3D&ppt=hp&ppn=homepage&ssid=8gsqcp4wqo0000001645498225412",
        "https://www.flipkart.com/boat-airdopes-131-bluetooth-headset/p/itmf76c6f983fbca?pid=ACCFSDGXX3S6DVBG&lid=LSTACCFSDGXX3S6DVBGSRHQQR&marketplace=FLIPKART&fm=personalisedRecommendation%2Fp2p-same&iid=R%3As%3Bp%3AACCFSDGSYTH8XV7A%3Bpt%3Ahp%3Buid%3Ac368e36e-938f-11ec-bec0-05e1cd695263%3B.ACCFSDGXX3S6DVBG&ppt=hp&ppn=homepage&otracker=hp_reco_More%2Bto%2BExplore_4_19.productCard.PMU_V2_boAt%2BAirdopes%2B131%2BBluetooth%2BHeadset_ACCFSDGXX3S6DVBG_personalisedRecommendation%2Fp2p-same_3&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2Fp2p-same_More%2Bto%2BExplore_DESKTOP_HORIZONTAL_productCard_cc_4_NA_view-all&cid=ACCFSDGXX3S6DVBG"]
    for i in URL_list:
        name, price = get_prices(i)
        print("name =", name)
        print("price = ", price)
        print("--------------------------------------")