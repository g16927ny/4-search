from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('top', views.search_top, name='search_top'),
    path('result/tokyo', views.search_result_tokyo, name='search_result_tokyo'),
    path('result/kanda', views.search_result_kanda, name='search_result_kanda'),
    path('result/ochanomizu', views.search_result_ochanomizu, name='search_result_ochanomizu'),
    path('result/suidobashi', views.search_result_suidobashi, name='search_result_suidobashi'),
    path('result/hacchobori', views.search_result_hacchobori, name='search_result_hacchobori'),
    path('result/ecchujima', views.search_result_ecchujima, name='search_result_ecchujima'),
    path('result/shiomi', views.search_result_shiomi, name='search_result_shiomi'),
    path('result/shinkiba', views.search_result_shinkiba, name='search_result_shinkiba'),
    path('result/kasairinkaikoen', views.search_result_kasairinkaikoen, name='search_result_kasairinkaikoen'),
    path('result/maihama', views.search_result_maihama, name='search_result_maihama'),
    path('result/shinurayasu', views.search_result_shinurayasu, name='search_result_shinurayasu'),
    path('result/ichikawashiohama', views.search_result_ichikawashiohama, name='search_result_ichikawashiohama'),
    path('result/hutamatashincho', views.search_result_hutamatashincho, name='search_result_hutamatashincho'),
    path('result/minamihunabashi', views.search_result_minamihunabashi, name='search_result_minamihunabashi'),
    path('result/shinnarashino', views.search_result_shinnarashino, name='search_result_shinnarashino'),
    path('result/kaihinmakuhari', views.search_result_kaihinmakuhari, name='search_result_kaihinmakuhari'),
    path('result/yotsuya', views.search_result_yotsuya, name='search_result_yotsuya'),
    path('result/shinjuku', views.search_result_shinjuku, name='search_result_shinjuku'),
    path('result/yoyogi', views.search_result_yoyogi, name='search_result_yoyogi'),
    path('result/kokuritsukyougijyo', views.search_result_kokuritsukyougijyo, name='search_result_kokuritsukyougijyo'),
    path('result/ootemachi', views.search_result_ootemachi, name='search_result_ootemachi'),
    path('result/jinbocho', views.search_result_jinbocho, name='search_result_jinbocho'),
    path('result/kudanshita', views.search_result_kudanshita, name='search_result_kudanshita'),
    path('result/yurakucho', views.search_result_yurakucho, name='search_result_yurakucho'),
    path('result/akihabara', views.search_result_akihabara, name='search_result_akihabara'),
    path('result/asakusabashi', views.search_result_asakusabashi, name='search_result_asakusabashi'),
    path('result/ryogoku', views.search_result_ryogoku, name='search_result_ryogoku'),
    path('result/shinagawa', views.search_result_shinagawa, name='search_result_shinagawa'),
    path('result/sengakuji', views.search_result_sengakuji, name='search_result_sengakuji'),
    path('result/mita', views.search_result_mita, name='search_result_mita'),
    path('result/shibakouen', views.search_result_shibakouen, name='search_result_shibakouen'),
    path('result/onarimachi', views.search_result_onarimachi, name='search_result_onarimachi'),
    path('result/uchisaiwaicho', views.search_result_uchisaiwaicho, name='search_result_uchisaiwaicho'),
    path('result/hibiya', views.search_result_hibiya, name='search_result_hibiya'),
    path('result/shinbashi', views.search_result_shinbashi, name='search_result_shinbashi'),
    path('result/takebashi', views.search_result_takebashi, name='search_result_takebashi'),
    path('result/tamachi', views.search_result_tamachi, name='search_result_tamachi'),
    path('result/hamamatsucho', views.search_result_hamamatsucho, name='search_result_hamamatsucho'),
    path('result/hanedakokunai', views.search_result_hanedakokunai, name='search_result_hanedakokunai'),
    path('result/hanedakokusai', views.search_result_hanedakokusai, name='search_result_hanedakokusai'),
    path('result/tenkubashi', views.search_result_tenkubashi, name='search_result_tenkubashi'),
    path('result/anamoriinari', views.search_result_anamoriinari, name='search_result_anamoriinari'),
    path('result/ootorii', views.search_result_ootorii, name='search_result_ootorii'),
    path('result/koujiya', views.search_result_koujiya, name='search_result_koujiya'),
    path('result/keikyukamata', views.search_result_keikyukamata, name='search_result_keikyukamata'),
    path('result/daimon', views.search_result_daimon, name='search_result_daimon'),
    path('result/akabanebashi', views.search_result_akabanebashi, name='search_result_akabanebashi'),
    path('result/azabujyuban', views.search_result_azabujyuban, name='search_result_azabujyuban'),
    path('result/roppongi', views.search_result_roppongi, name='search_result_roppongi'),
    path('result/aoyamaicchome', views.search_result_aoyamaicchome, name='search_result_aoyamaicchome'),
    path('result/higashiginza', views.search_result_higashiginza, name='search_result_higashiginza'),
    path('result/takaracho', views.search_result_takaracho, name='search_result_takaracho'),
    path('result/nihonbashi', views.search_result_nihonbashi, name='search_result_nihonbashi'),
    path('result/naritakuko', views.search_result_naritakuko, name='search_result_naritakuko'),
    path('result/kukodainibiru', views.search_result_kukodainibiru, name='search_result_kukodainibiru'),
    path('result/nippori', views.search_result_nippori, name='search_result_nippori'),
    path('result/uguisudani', views.search_result_uguisudani, name='search_result_uguisudani'),
    path('result/ueno', views.search_result_ueno, name='search_result_ueno'),
    path('result/okachimachi', views.search_result_okachimachi, name='search_result_okachimachi'),
    path('result/iidabashi', views.search_result_iidabashi, name='search_result_iidabashi'),
    path('result/ichigaya', views.search_result_ichigaya, name='search_result_ichigaya'),
    path('result/shinanomachi', views.search_result_shinanomachi, name='search_result_shinanomachi'),
    path('result/sendagaya', views.search_result_sendagaya, name='search_result_sendagaya'),
    path('result/awajicho', views.search_result_awajicho, name='search_result_awajicho'),
    path('result/hongosanchome', views.search_result_hongosanchome, name='search_result_hongosanchome'),
    path('result/kourakuen', views.search_result_kourakuen, name='search_result_kourakuen'),
    path('result/uenookachimachi', views.search_result_uenookachimachi, name='search_result_uenookachimachi'),
    path('result/kuramae', views.search_result_kuramae, name='search_result_kuramae'),
    path('result/osaki', views.search_result_osaki, name='search_result_osaki'),
    path('result/gotanda', views.search_result_gotanda, name='search_result_gotanda'),
    path('result/meguro', views.search_result_meguro, name='search_result_meguro'),
    path('result/ebisu', views.search_result_ebisu, name='search_result_ebisu'),
    path('result/shibuya', views.search_result_shibuya, name='search_result_shibuya'),
    path('result/harajuku', views.search_result_harajuku, name='search_result_harajuku'),
    path('result/toranomon', views.search_result_toranomon, name='search_result_toranomon'),
    path('result/tameikesannou', views.search_result_tameikesannou, name='search_result_tameikesannou'),
    path('result/akasakamitsuke', views.search_result_akasakamitsuke, name='search_result_akasakamitsuke'),
    path('result/nagatacho', views.search_result_nagatacho, name='search_result_nagatacho'),
    path('result/hanzomon', views.search_result_hanzomon, name='search_result_hanzomon'),
    path('result/shiodome', views.search_result_shiodome, name='search_result_shiodome'),
    path('result/tsukidisijyo', views.search_result_tsukidisijyo, name='search_result_tsukidisijyo'),
    path('result/kachidoki', views.search_result_kachidoki, name='search_result_kachidoki'),
    path('result/tsukishima', views.search_result_tsukishima, name='search_result_tsukishima'),
    path('result/monzennakamachi', views.search_result_monzennakamachi, name='search_result_monzennakamachi'),
    path('result/kiyosumishirakawa', views.search_result_kiyosumishirakawa, name='search_result_kiyosumishirakawa'),
    path('result/morishita', views.search_result_morishita, name='search_result_morishita'),
    path('result/omotesando', views.search_result_omotesando, name='search_result_omotesando'),
    path('result/keiseiueno', views.search_result_keiseiueno, name='search_result_keiseiueno'),
    path('result/uenohirokouji', views.search_result_uenohirokouji, name='search_result_uenohirokouji'),
    path('result/suehirocho', views.search_result_suehirocho, name='search_result_suehirocho'),
    path('result/mitsukoshimae', views.search_result_mitsukoshimae, name='search_result_mitsukoshimae'),
    path('result/narita', views.search_result_narita, name='search_result_narita'),
    path('result/shisui', views.search_result_shisui, name='search_result_shisui'),
    path('result/sakura', views.search_result_sakura, name='search_result_sakura'),
    path('result/monoi', views.search_result_monoi, name='search_result_monoi'),
    path('result/yotsukaidou', views.search_result_yotsukaidou, name='search_result_yotsukaidou'),
    path('result/tsuga', views.search_result_tsuga, name='search_result_tsuga'),
    path('result/chiba', views.search_result_chiba, name='search_result_chiba'),
    path('result/inage', views.search_result_inage, name='search_result_inage'),
    path('result/tsudanuma', views.search_result_tsudanuma, name='search_result_tsudanuma'),
    path('result/hunabashi', views.search_result_hunabashi, name='search_result_hunabashi'),
    path('result/ichikawa', views.search_result_ichikawa, name='search_result_ichikawa'),
    path('result/shinkoiwa', views.search_result_shinkoiwa, name='search_result_shinkoiwa'),
    path('result/kinshicho', views.search_result_kinshicho, name='search_result_kinshicho'),
    path('result/keiseinarita', views.search_result_keiseinarita, name='search_result_keiseinarita'),
    path('result/koudunomori', views.search_result_koudunomori, name='search_result_koudunomori'),
    path('result/sougosando', views.search_result_sougosando, name='search_result_sougosando'),
    path('result/keiseishisui', views.search_result_keiseishisui, name='search_result_keiseishisui'),
    path('result/oosakura', views.search_result_oosakura, name='search_result_oosakura'),
    path('result/keiseisakura', views.search_result_keiseisakura, name='search_result_keiseisakura'),
    path('result/katsutadai', views.search_result_katsutadai, name='search_result_katsutadai'),
    path('result/yachiyodai', views.search_result_yachiyodai, name='search_result_yachiyodai'),
    path('result/keiseitudanuma', views.search_result_keiseitudanuma, name='search_result_keiseitudanuma'),
    path('result/yatsu', views.search_result_yatsu, name='search_result_yatsu'),
    path('result/hunabashikeibajyo', views.search_result_hunabashikeibajyo, name='search_result_hunabashikeibajyo'),
    path('result/daijingushita', views.search_result_daijingushita, name='search_result_daijingushita'),
    path('result/keiseihunabashi', views.search_result_keiseihunabashi, name='search_result_keiseihunabashi'),
    path('result/kaijin', views.search_result_kaijin, name='search_result_kaijin'),
    path('result/keiseinishihuna', views.search_result_keiseinishihuna, name='search_result_keiseinishihuna'),
    path('result/nishihunabashi', views.search_result_nishihunabashi, name='search_result_nishihunabashi'),
    path('result/touyoucho', views.search_result_touyoucho, name='search_result_touyoucho'),
    path('result/kiba', views.search_result_kiba, name='search_result_kiba'),
    path('result/monzennakamachi', views.search_result_monzennakamachi, name='search_result_monzennakamachi'),
    path('result/kayabacho', views.search_result_kayabacho, name='search_result_kayabacho'),
    path('result/nihonbashi', views.search_result_nihonbashi, name='search_result_nihonbashi'),
    path('result/keiseiyahata', views.search_result_keiseiyahata, name='search_result_keiseiyahata'),
    path('result/keiseitakasago', views.search_result_keiseitakasago, name='search_result_keiseitakasago'),
    path('result/aoto', views.search_result_aoto, name='search_result_aoto'),
    path('result/keiseitateishi', views.search_result_keiseitateishi, name='search_result_keiseitateishi'),
    path('result/yotsugi', views.search_result_yotsugi, name='search_result_yotsugi'),
    path('result/yahiro', views.search_result_yahiro, name='search_result_yahiro'),
    path('result/keiseihikihune', views.search_result_keiseihikihune, name='search_result_keiseihikihune'),
    path('result/oshiage', views.search_result_oshiage, name='search_result_oshiage'),
    path('result/honjoaduma', views.search_result_honjoaduma, name='search_result_honjoaduma'),
    path('result/asakusa', views.search_result_asakusa, name='search_result_asakusa'),
    path('result/ningyocho', views.search_result_ningyocho, name='search_result_ningyocho'),
    path('result/higashinihonbashi', views.search_result_higashinihonbashi, name='search_result_higashinihonbashi'),
    path('result/bakuroyokoyama', views.search_result_bakuroyokoyama, name='search_result_bakuroyokoyama'),
    path('result/iwamotocho', views.search_result_iwamotocho, name='search_result_iwamotocho'),
    path('result/ogawacho', views.search_result_ogawacho, name='search_result_ogawacho'),
    path('result/nishichiba', views.search_result_nishichiba, name='search_result_nishichiba'),
    path('result/shinkemigawa', views.search_result_shinkemigawa, name='search_result_shinkemigawa'),
    path('result/makuharihongou', views.search_result_makuharihongou, name='search_result_makuharihongou'),
    path('result/shimousanakayama', views.search_result_shimousanakayama, name='search_result_shimousanakayama'),
    path('result/honyahata', views.search_result_honyahata, name='search_result_honyahata'),
    path('result/koiwa', views.search_result_koiwa, name='search_result_koiwa'),
    path('result/hirai', views.search_result_hirai, name='search_result_hirai'),
    path('result/kameido', views.search_result_kameido, name='search_result_kameido')


]