from django.shortcuts import redirect
from django.shortcuts import render, get_list_or_404
from django.shortcuts import render, get_object_or_404
from .models import Hotel

#from .forms import HotelForm

def search_top(request):
    d = {
    'depselect': request.GET.get('depselect'),
    'desselect': request.GET.get('desselect')
    }
    return render(request, 'search/search_top.html', d)

def search_result_tokyo(request):
    hotels = get_list_or_404(Hotel, nearstation='東京')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_kanda(request):
    hotels = get_list_or_404(Hotel, nearstation='神田')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_ochanomizu(request):
    hotels = get_list_or_404(Hotel, nearstation='御茶ノ水')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_suidobashi(request):
    hotels = get_list_or_404(Hotel, nearstation='水道橋')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_hacchobori(request):
    hotels = get_list_or_404(Hotel, nearstation='八丁堀')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_ecchujima(request):
    hotels = get_list_or_404(Hotel, nearstation='越中島')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_shiomi(request):
    hotels = get_list_or_404(Hotel, nearstation='潮見')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_shinkiba(request):
    hotels = get_list_or_404(Hotel, nearstation='新木場')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_kasairinkaikoen(request):
    hotels = get_list_or_404(Hotel, nearstation='葛西臨海公園')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_maihama(request):
    hotels = get_list_or_404(Hotel, nearstation='舞浜')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_shinurayasu(request):
    hotels = get_list_or_404(Hotel, nearstation='新浦安')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_ichikawashiohama(request):
    hotels = get_list_or_404(Hotel, nearstation='市川塩浜')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_hutamatashincho(request):
    hotels = get_list_or_404(Hotel, nearstation='二俣新町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_minamihunabashi(request):
    hotels = get_list_or_404(Hotel, nearstation='南船橋')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_shinnarashino(request):
    hotels = get_list_or_404(Hotel, nearstation='新習志野')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_kaihinmakuhari(request):
    hotels = get_list_or_404(Hotel, nearstation='海浜幕張')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_yotsuya(request):
    hotels = get_list_or_404(Hotel, nearstation='四ツ谷')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_shinjuku(request):
    hotels = get_list_or_404(Hotel, nearstation='新宿')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_yoyogi(request):
    hotels = get_list_or_404(Hotel, nearstation='代々木')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_kokuritsukyougijyo(request):
    hotels = get_list_or_404(Hotel, nearstation='国立競技場')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_ootemachi(request):
    hotels = get_list_or_404(Hotel, nearstation='大手町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_jinbocho(request):
    hotels = get_list_or_404(Hotel, nearstation='神保町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_kudanshita(request):
    hotels = get_list_or_404(Hotel, nearstation='九段下')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_yurakucho(request):
    hotels = get_list_or_404(Hotel, nearstation='有楽町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_akihabara(request):
    hotels = get_list_or_404(Hotel, nearstation='秋葉原')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_asakusabashi(request):
    hotels = get_list_or_404(Hotel, nearstation='浅草橋')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_ryogoku(request):
    hotels = get_list_or_404(Hotel, nearstation='両国')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_shinagawa(request):
    hotels = get_list_or_404(Hotel, nearstation='品川')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_sengakuji(request):
    hotels = get_list_or_404(Hotel, nearstation='泉岳寺')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_mita(request):
    hotels = get_list_or_404(Hotel, nearstation='三田')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_shibakouen(request):
    hotels = get_list_or_404(Hotel, nearstation='芝公園')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_onarimachi(request):
    hotels = get_list_or_404(Hotel, nearstation='御成町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_uchisaiwaicho(request):
    hotels = get_list_or_404(Hotel, nearstation='内幸町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_hibiya(request):
    hotels = get_list_or_404(Hotel, nearstation='日比谷')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_shinbashi(request):
    hotels = get_list_or_404(Hotel, nearstation='新橋')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_takebashi(request):
    hotels = get_list_or_404(Hotel, nearstation='竹橋')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_tamachi(request):
    hotels = get_list_or_404(Hotel, nearstation='田町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_hamamatsucho(request):
    hotels = get_list_or_404(Hotel, nearstation='浜松町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_hanedakokunai(request):
    hotels = get_list_or_404(Hotel, nearstation='羽田空港国内線ターミナル')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_hanedakokusai(request):
    hotels = get_list_or_404(Hotel, nearstation='羽田空港国際線ターミナル')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_tenkubashi(request):
    hotels = get_list_or_404(Hotel, nearstation='天空橋')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_anamoriinari(request):
    hotels = get_list_or_404(Hotel, nearstation='穴守稲荷')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_ootorii(request):
    hotels = get_list_or_404(Hotel, nearstation='大鳥居')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_koujiya(request):
    hotels = get_list_or_404(Hotel, nearstation='糀谷')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_keikyukamata(request):
    hotels = get_list_or_404(Hotel, nearstation='京急蒲田')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_daimon(request):
    hotels = get_list_or_404(Hotel, nearstation='大門')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_akabanebashi(request):
    hotels = get_list_or_404(Hotel, nearstation='赤羽橋')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_azabujyuban(request):
    hotels = get_list_or_404(Hotel, nearstation='麻布十番')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_roppongi(request):
    hotels = get_list_or_404(Hotel, nearstation='六本木')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_aoyamaicchome(request):
    hotels = get_list_or_404(Hotel, nearstation='青山一丁目')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_higashiginza(request):
    hotels = get_list_or_404(Hotel, nearstation='東銀座')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_takaracho(request):
    hotels = get_list_or_404(Hotel, nearstation='宝町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_nihonbashi(request):
    hotels = get_list_or_404(Hotel, nearstation='日本橋')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_naritakuko(request):
    hotels = get_list_or_404(Hotel, nearstation='成田空港')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_kukodainibiru(request):
    hotels = get_list_or_404(Hotel, nearstation='空港第二ビル')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_nippori(request):
    hotels = get_list_or_404(Hotel, nearstation='日暮里')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_uguisudani(request):
    hotels = get_list_or_404(Hotel, nearstation='鶯谷')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_ueno(request):
    hotels = get_list_or_404(Hotel, nearstation='上野')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_okachimachi(request):
    hotels = get_list_or_404(Hotel, nearstation='御徒町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_iidabashi(request):
    hotels = get_list_or_404(Hotel, nearstation='飯田橋')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_ichigaya(request):
    hotels = get_list_or_404(Hotel, nearstation='市ヶ谷')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_shinanomachi(request):
    hotels = get_list_or_404(Hotel, nearstation='信濃町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_sendagaya(request):
    hotels = get_list_or_404(Hotel, nearstation='千駄ヶ谷')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_awajicho(request):
    hotels = get_list_or_404(Hotel, nearstation='淡路町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_hongosanchome(request):
    hotels = get_list_or_404(Hotel, nearstation='本郷三丁目')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_kourakuen(request):
    hotels = get_list_or_404(Hotel, nearstation='後楽園')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_uenookachimachi(request):
    hotels = get_list_or_404(Hotel, nearstation='上野御徒町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_kuramae(request):
    hotels = get_list_or_404(Hotel, nearstation='蔵前')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_osaki(request):
    hotels = get_list_or_404(Hotel, nearstation='大崎')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_gotanda(request):
    hotels = get_list_or_404(Hotel, nearstation='五反田')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_meguro(request):
    hotels = get_list_or_404(Hotel, nearstation='目黒')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_ebisu(request):
    hotels = get_list_or_404(Hotel, nearstation='恵比寿')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_shibuya(request):
    hotels = get_list_or_404(Hotel, nearstation='渋谷')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_harajuku(request):
    hotels = get_list_or_404(Hotel, nearstation='原宿')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_toranomon(request):
    hotels = get_list_or_404(Hotel, nearstation='虎ノ門')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_tameikesannou(request):
    hotels = get_list_or_404(Hotel, nearstation='溜池山王')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_akasakamitsuke(request):
    hotels = get_list_or_404(Hotel, nearstation='赤坂見附')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_nagatacho(request):
    hotels = get_list_or_404(Hotel, nearstation='永田町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_hanzomon(request):
    hotels = get_list_or_404(Hotel, nearstation='半蔵門')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_shiodome(request):
    hotels = get_list_or_404(Hotel, nearstation='汐留')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_tsukidisijyo(request):
    hotels = get_list_or_404(Hotel, nearstation='築地市場')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_kachidoki(request):
    hotels = get_list_or_404(Hotel, nearstation='勝どき')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_tsukishima(request):
    hotels = get_list_or_404(Hotel, nearstation='月島')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_monzennakamachi(request):
    hotels = get_list_or_404(Hotel, nearstation='門前仲町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_kiyosumishirakawa(request):
    hotels = get_list_or_404(Hotel, nearstation='清澄白河')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_morishita(request):
    hotels = get_list_or_404(Hotel, nearstation='森下')
    return render(request, 'search/search_result.html', {'hotels': hotels})


def search_result_omotesando(request):
    hotels = get_list_or_404(Hotel, nearstation='表参道')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_keiseiueno(request):
    hotels = get_list_or_404(Hotel, nearstation='京成上野')
    return render(request, 'search/search_result.html', {'hotels': hotels})


def search_result_uenohirokouji(request):
    hotels = get_list_or_404(Hotel, nearstation='上野広小路')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_suehirocho(request):
    hotels = get_list_or_404(Hotel, nearstation='末広町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_mitsukoshimae(request):
    hotels = get_list_or_404(Hotel, nearstation='三越前')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_narita(request):
    hotels = get_list_or_404(Hotel, nearstation='成田')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_shisui(request):
    hotels = get_list_or_404(Hotel, nearstation='酒々井')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_sakura(request):
    hotels = get_list_or_404(Hotel, nearstation='佐倉')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_monoi(request):
    hotels = get_list_or_404(Hotel, nearstation='物井')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_yotsukaidou(request):
    hotels = get_list_or_404(Hotel, nearstation='四街道')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_tsuga(request):
    hotels = get_list_or_404(Hotel, nearstation='都賀')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_chiba(request):
    hotels = get_list_or_404(Hotel, nearstation='千葉')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_inage(request):
    hotels = get_list_or_404(Hotel, nearstation='稲毛')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_tsudanuma(request):
    hotels = get_list_or_404(Hotel, nearstation='津田沼')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_hunabashi(request):
    hotels = get_list_or_404(Hotel, nearstation='船橋')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_ichikawa(request):
    hotels = get_list_or_404(Hotel, nearstation='市川')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_shinkoiwa(request):
    hotels = get_list_or_404(Hotel, nearstation='新小岩')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_kinshicho(request):
    hotels = get_list_or_404(Hotel, nearstation='錦糸町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_keiseinarita(request):
    hotels = get_list_or_404(Hotel, nearstation='京成成田')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_koudunomori(request):
    hotels = get_list_or_404(Hotel, nearstation='公津の杜')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_sougosando(request):
    hotels = get_list_or_404(Hotel, nearstation='宗吾参道')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_keiseishisui(request):
    hotels = get_list_or_404(Hotel, nearstation='京成酒々井')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_oosakura(request):
    hotels = get_list_or_404(Hotel, nearstation='大佐倉')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_keiseisakura(request):
    hotels = get_list_or_404(Hotel, nearstation='京成佐倉')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_katsutadai(request):
    hotels = get_list_or_404(Hotel, nearstation='勝田台')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_yachiyodai(request):
    hotels = get_list_or_404(Hotel, nearstation='八千代台')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_keiseitudanuma(request):
    hotels = get_list_or_404(Hotel, nearstation='京成津田沼')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_yatsu(request):
    hotels = get_list_or_404(Hotel, nearstation='谷津')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_hunabashikeibajyo(request):
    hotels = get_list_or_404(Hotel, nearstation='船橋競馬場')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_daijingushita(request):
    hotels = get_list_or_404(Hotel, nearstation='大神宮下')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_keiseihunabashi(request):
    hotels = get_list_or_404(Hotel, nearstation='京成船橋')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_kaijin(request):
    hotels = get_list_or_404(Hotel, nearstation='海神')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_keiseinishihuna(request):
    hotels = get_list_or_404(Hotel, nearstation='京成西船')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_nishihunabashi(request):
    hotels = get_list_or_404(Hotel, nearstation='西船橋')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_touyoucho(request):
    hotels = get_list_or_404(Hotel, nearstation='東陽町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_kiba(request):
    hotels = get_list_or_404(Hotel, nearstation='木場')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_monzennakamachi(request):
    hotels = get_list_or_404(Hotel, nearstation='門前仲町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_kayabacho(request):
    hotels = get_list_or_404(Hotel, nearstation='茅場町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_nihonbashi(request):
    hotels = get_list_or_404(Hotel, nearstation='日本橋')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_keiseiyahata(request):
    hotels = get_list_or_404(Hotel, nearstation='京成八幡')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_keiseitakasago(request):
    hotels = get_list_or_404(Hotel, nearstation='京成高砂')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_aoto(request):
    hotels = get_list_or_404(Hotel, nearstation='青砥')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_keiseitateishi(request):
    hotels = get_list_or_404(Hotel, nearstation='京成立石')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_yotsugi(request):
    hotels = get_list_or_404(Hotel, nearstation='四ツ木')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_yahiro(request):
    hotels = get_list_or_404(Hotel, nearstation='八広')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_keiseihikihune(request):
    hotels = get_list_or_404(Hotel, nearstation='京成曳舟')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_oshiage(request):
    hotels = get_list_or_404(Hotel, nearstation='押上')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_honjoaduma(request):
    hotels = get_list_or_404(Hotel, nearstation='本所吾妻橋')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_asakusa(request):
    hotels = get_list_or_404(Hotel, nearstation='浅草')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_ningyocho(request):
    hotels = get_list_or_404(Hotel, nearstation='人形町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_higashinihonbashi(request):
    hotels = get_list_or_404(Hotel, nearstation='東日本橋')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_bakuroyokoyama(request):
    hotels = get_list_or_404(Hotel, nearstation='馬喰横山')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_iwamotocho(request):
    hotels = get_list_or_404(Hotel, nearstation='岩本町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_ogawacho(request):
    hotels = get_list_or_404(Hotel, nearstation='小川町')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_nishichiba(request):
    hotels = get_list_or_404(Hotel, nearstation='西千葉')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_shinkemigawa(request):
    hotels = get_list_or_404(Hotel, nearstation='新検見川')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_makuharihongou(request):
    hotels = get_list_or_404(Hotel, nearstation='幕張本郷')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_shimousanakayama(request):
    hotels = get_list_or_404(Hotel, nearstation='下総中山')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_honyahata(request):
    hotels = get_list_or_404(Hotel, nearstation='本八幡')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_koiwa(request):
    hotels = get_list_or_404(Hotel, nearstation='小岩')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_hirai(request):
    hotels = get_list_or_404(Hotel, nearstation='平井')
    return render(request, 'search/search_result.html', {'hotels': hotels})

def search_result_kameido(request):
    hotels = get_list_or_404(Hotel, nearstation='亀戸')
    return render(request, 'search/search_result.html', {'hotels': hotels})
