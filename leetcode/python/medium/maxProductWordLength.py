'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
    Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    Return 16
    The two words can be "abcw", "xtfn".
'''
def noLetterInCommon(str1, str2):
    for l in str1:
        if l in str2:
            return False

    return True

def maxProduct(words):
    """
    :type words: List[str]
    :rtype: int
    """
    words.sort(key = lambda s: len(s))
    print len(words)
    if len(words) < 2:
        return 0
    max_possible_sum = 0
    for i in range(len(words) - 1, 0, -1):
        for j in range(i - 1, 0, -1):
            if len(words[i]) * len(words[j]) > 59:
                print words[i], words[j], noLetterInCommon(words[i], words[j]), len(words[i]) * len(words[j])
            if noLetterInCommon(words[i], words[j]):
                print words[i], words[j], noLetterInCommon(words[i], words[j])
                if len(words[i]) * len(words[j]) > max_possible_sum:
                    print 'max_possible_sum, len(words[i]) * len(words[j])', max_possible_sum, len(words[i]) * len(words[j])
                    max_possible_sum = len(words[i]) * len(words[j])

    return max_possible_sum

words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
words1 = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
words3 = ["a", "aa", "aaa", "aaaa"]
words4 = ["bcedengp","jegidiicfohjimcccnkagmanbkkmbmlfabgammipaiepjnfi","condccpkmicalappldjbnlepdplggcmcnilkkinefgdmldegcjbimfaikfjldpoplcakdkglpnlnjkojhcglig","gnpddclieoneddfhojknjkkaehlkgegpfbnopjcnogcicokhlffd","edjnfgmoaningkmcfncodeganbmbhamoighbojdcjcdicipdobbcahil","hkjkfjkmaagcgpcimmljfghmkgekmkh","homffkkkipepcbmipn","ipkakmolkhecdddpdpcphafiaofgb","jeejnmdgokbmkmpdlkgiolkemenahkoidimoeidpagefpcokodcmjdjcbkaeaogmcbenhdcnegg","eapffhadafnnalkkobdbmpnnhfeg","opfknkinpknipgjhcjdgffjoippjcnfabdejn","fhnpojhnfiogkdgffgjc","nlhmgmigpbconl","jjlejejegngdljbgkkomfacjfjoemilaeofgdhiip","imagjifpapmgej","mjkdjbjmbhfbkbjnahlenhkdnnpplpenidahdkokeihmjjfojndiidlbkh","ihpnbcncpigllmpdekkjbdemobbdjemafeioiaoibgabakmmkklopoeppibdfhdlallcedldclmkhpmkkdg","plfpneanjljoebogkbfabdnkanodgljecaemcffnoicmdbgkkfma","afianbgmdff","bhobekifemheldcamckoccfdcnmdcmnfbodfldbhgoikplggehfokkolacadgoholcdbgcpgoanmmnmika","bnjklpaiklipbcbphhfjoibhhhljoppcfjdno","ickghheki","kacnagbficmhikbdeldcagg","laamledghhflcjjdfofdojkfbkl","aacafidfbpmimlclhcjignenchbdjcgfbdiegmohfloieajekfgcmamifbmkjnoaipcfmbejmkigaekcgemffemfcnkhhkkj","hlcdacefjodhllpbhkkokepmcdmmigclefoglahalejfiipjelmhkbhjblmbkgpimjbmplmgclfiifncckibpkjlnkbgcph","ohdadlaokhbhlgiepimmdmfegefpbkbcodnfebbcfakfijhnefg","lgeokomognpmfblbhekgnlpdohnpkoajionmjhhagenafmcdpgfiidlmnogigfipdpgjljlgakaoammekhmjhecnmghecdhljl","kmjkfdbibcnkinkagennlcfbajffdkgajloinjakombekjcbh","iofimmgddmjidfmmloofkdihlffaakapkhchmcclocdbandon","kpbmkbdfgobjebadjdhgkglakcbjpjkkpd","ghjahnmogdofblllfpdfbhohkmdingfmaofoflchbhpkjccffadnbd","lobkhmbgcjdpkemkijhddofpadcgabbfadkhmdmgippceaapeabhbemoejfhejhjncceckddmldpbdlmeljmcpbnaflolihhaojlp","nlcmhaaebniidhgammlkhpphglanihnmpchebbehfgjeegdkicbnnkgnaipdhiemigfgaoehedph","ecdnklamhjbkemhngkldlbbbkalepnlci","eokamphdgfobplgmnhcigcjalmbldgmfcgbppcicooneopcmkginofpcmgleeplobcd","fcmjlicbblmgpoedaglfpdmiajjnfjdlklfoapdigokimnjfnboecnlejeklcifhoomlnmlfimmjdpfieamjnmmcklcflmjd","dnfkclagfkofamkdijjhhklenidoahjeoieaddohalfdbkjgfeojdonnnpbpnkofhafohinchffihnkmcdbhnfano","jajcnlbijmpkhmninjpdjlaiabdpeinep","lpffenbmipjalpmocceaegabghkkbldmaaef","hfnjdgjcllcepegpgebbdiod","blofdnemnlghmhnklnagnjdhhncbligogkmcankckkicohicfocenpdfojnkkbfaihbfkceclmnj","blkojdljgkfbgoocagophckjhhaedplcecjhni","bfbmhobnbpjipgnohnnggkodlnhnpdnnjjodjjhjpoiblenkmmjfn","dakooapcaocdjjlohkhodebfljekmohmhaajabfmfpkmgenpcgejdmbpfhdmjcndidgnckejn","mcdplfipobaabeljedjjgffgibkjkfhcknlelcjploff","hfkkkgc","bckkahmfgpmllpjlegffdhmamighjeejfeibomlcflnf","hdlfkfnncgfggofkhbnnoogdhcjbmiecemdhblmaclcjjhfkd","hlleonkggomlodjiicahjpacmfmnjfhefghfjfjjhmollnmceckfl","fikabchalojpfe","eabebmiboflaoeilplfgbodlnpdjdiigcchpimdmgmimfdallmcig","piaaepcaceeiiejnliffickdbjnpbfggbdlcjcbggmbfegohjnnemkbjiaamcnplelnmlfjcab","olaganiohokddaakddildkphfmohabaneglhkapeeefkjdcb","obknlbdepjhofdgpjmbiefollhjdmkcgiembmcejbekalcdfpmdmpedblmodhkgmdnneheegkebc","fbelnnohpboamjkbddhlbcdllnlkgllkafiionmipaafpeibf","cdmdiekekdfagofmfnffnclcfjajllhojglodmpiaffddknehallhoojhjmgjifeofmagdjfengmpohechphnkghdjhmnldh","bfjegjnfdeipaogfeifnnpgpbblfdc","poenmckimbpifflnjcnejemhjdifmibniogckajponoamnoldfefdoglmhlldicekiecnmomp","nbchhcmpbialmi","jdebllagcaidnkmbbadfmnjjhiondmphngmmdkjmbmfecfdhhggmllmnjicdokbiekbpmkebhhcjjbolcppnomldpckdfij","dbbjijglkgaomhphbfpaejiiknadcoaopo","gdcakpbpcpeebncijnldoigfnm","njkhafdm","hahieknapoaidphimlidackdnhhdcnlfhhahjfdkacbdfdfeeogeklcfmmlfeiamjfpmbaiolgcgoncandlcabahfmdk","iagkkbchfijjnjggeiipikldigbinhdoppcaldcbognoakidpppchhdknedhlfmgmgmkombekejdigiimoefmahmahhhgdcm","jkpkfmpgfknpicjkodpjhmfhiikgdifapoldfojbahpbjbgdhiookababepckambnc","afcaeklcpjhjfampafogehdpiianokcpclohciajpmbaplgfpkjnkallpkoghglaccnfhnllkinigchddaak","hmkbgninnnmebgaghblo","npfpcpfekkcmb","dchjgnnbbdhllkdihdcdpkjdjmhnamjpfjalnambcpfmlahocemncmhoockmgedlegcfjnomdo","mh","kbbibjkm","fiopkjgdgpodnkpiekggelkhblbkeaoekdfpomgmcijfchankfmffiacafkcnbpp","pcemmimjiipcaimpipmpachpjlnpmdoneiag","ceoeipfliflfjnmpkngcoidgjicpapfaogiegfbhgpflnbjbgpencgaopmepkmfnkkjblphcgabbincgajfgelapmhjloefpogkpp","clockpjegiikjgkgjofgdgbjejknn","kjkjklbhfdmjmhnpmjoehniigbmofjmbmjkfmcahpgabamahpmimgicbfoemfomgdifoajmlnjbpbdfcilcidibhejkkbbhe","egkjneklne","aohokpnbnjchkkfipbfpjcbmnpebdklngnmfjaj","fhcnhadlelgajengoocmcjfmglpanhiciffmikjjgiboblmcbfomkdlkhpeoidfgemhccpogimlnpdemfia","jbemhdfkcoldoanpmedafkbpmnnfmhdmlncciojcmecoglahffmgkhgpofeegoebdnlfpebgapbflcma","hfhbipcidfdfgbhhmahnfgpliagmolhhfbmcjfgnhkdkale","nllcogabcbbfggkknkjimmbdlfinamdifcbgoffhekkhpfflpfnleccapgcepgankpnblofmphplpnomfdkdbcdhejp","dgpjgjnagacjfhlkhnmpfbhcplfehoolafmpieoh","mcjhhgajmclkoiobmgaaellbekaadlkopgbkobmmipeollfcjgo","lhnlcgljdpcbcjmncpiojli","obcddnfdiogpchomf","kjhkbnpcphmpnpilkhbjmeohodcoonanlmniifpiiiipcegagnhpbpfadgo","cjbakbbjaikfjnbimkeifcoinhhkcogokknajeagmfkcldfijhhfapnnjnljnecknlgdmapnlhffdndahoj","hdpflnimifempccgjolbdbdalfaapfijpmjnkaedkgmbpanmilleeahmnpiipna","cpjkhblnleglklhhdolggpgfmgahhilhbjgdhegkkeppiibnif","cldhiemiaoeaahi","cnjbbeedhddcjcelhcmfnmfcmpo","piekkbklhnpokeeiidbhbcjfgmddkejhdhfcenabobmjleemneikgkjokmcikiemgjhdmjcni","lknlpnlnnck","hgooknomoahjpebbcnidnagdfghooihkhjmeadhbojodhfkgkcbgmcbfkeammfhnlpbmoggfcgbcmfllalal","jljohilkaekocjcfdmpjgcpbpolfobdpmojcpmphlpnedaheholbbpdnnfoibpacmjmgglboodfoldicnjmodcipa","colgmamhgjeckgiiehibkipdl","afiljflhejeanlimdhcicfebapebcfefchdadfchfklcdgbkmagpkofpnphhhpbbpebkabdppocfbag"]
print maxProduct(words4)
#print maxProduct(words) 
#print maxProduct(words1)
#print maxProduct(words3)
        
