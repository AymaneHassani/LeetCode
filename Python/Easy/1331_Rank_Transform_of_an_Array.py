"""
Date: October 2, 2024
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
 

Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
Example 2:

Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.
Example 3:

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]
 

Constraints:

0 <= arr.length <= 105
-109 <= arr[i] <= 109
"""
from typing import List
class Solution:    
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        Given an array of integers arr, replace each element with its rank.
        The rank represents how large the element is. If two elements are equal, they share the same rank.
        The smallest element gets the rank 1, the second smallest gets rank 2, and so on.
        
        Parameters:
        arr (List[int]): List of integers to transform
        
        Returns:
        List[int]: List of ranks corresponding to the elements of arr
        """
        # Step 1: Create a sorted list of unique elements from arr
        sorted_unique = sorted(set(arr)) 
        
        # Step 2: Create a dictionary to map each unique value to its rank
        value_to_rank = {value: rank for rank, value in enumerate(sorted_unique, start=1)} 
        
        # Step 3: Transform the original array by replacing each value with its rank
        return [value_to_rank[value] for value in arr]

### Unit Testing
if __name__ == "__main__":
    assert Solution().arrayRankTransform([100,100,100]) == [1, 1, 1]
    assert Solution().arrayRankTransform([40,10,20,30]) == [4, 1, 2, 3]
    assert Solution().arrayRankTransform([37,12,28,9,100,56,80,5,12]) == [5,3,4,2,8,6,7,1,3]
    assert Solution().arrayRankTransform([1000,999,998,997,996,995,994,993,992,991,990,989,988,987,986,985,984,983,982,981,980,979,978,977,976,975,974,973,972,971,970,969,968,967,966,965,964,963,962,961,960,959,958,957,956,955,954,953,952,951,950,949,948,947,946,945,944,943,942,941,940,939,938,937,936,935,934,933,932,931,930,929,928,927,926,925,924,923,922,921,920,919,918,917,916,915,914,913,912,911,910,909,908,907,906,905,904,903,902,901,900,899,898,897,896,895,894,893,892,891,890,889,888,887,886,885,884,883,882,881,880,879,878,877,876,875,874,873,872,871,870,869,868,867,866,865,864,863,862,861,860,859,858,857,856,855,854,853,852,851,850,849,848,847,846,845,844,843,842,841,840,839,838,837,836,835,834,833,832,831,830,829,828,827,826,825,824,823,822,821,820,819,818,817,816,815,814,813,812,811,810,809,808,807,806,805,804,803,802,801,800,799,798,797,796,795,794,793,792,791,790,789,788,787,786,785,784,783,782,781,780,779,778,777,776,775,774,773,772,771,770,769,768,767,766,765,764,763,762,761,760,759,758,757,756,755,754,753,752,751,750,749,748,747,746,745,744,743,742,741,740,739,738,737,736,735,734,733,732,731,730,729,728,727,726,725,724,723,722,721,720,719,718,717,716,715,714,713,712,711,710,709,708,707,706,705,704,703,702,701,700,699,698,697,696,695,694,693,692,691,690,689,688,687,686,685,684,683,682,681,680,679,678,677,676,675,674,673,672,671,670,669,668,667,666,665,664,663,662,661,660,659,658,657,656,655,654,653,652,651,650,649,648,647,646,645,644,643,642,641,640,639,638,637,636,635,634,633,632,631,630,629,628,627,626,625,624,623,622,621,620,619,618,617,616,615,614,613,612,611,610,609,608,607,606,605,604,603,602,601,600,599,598,597,596,595,594,593,592,591,590,589,588,587,586,585,584,583,582,581,580,579,578,577,576,575,574,573,572,571,570,569,568,567,566,565,564,563,562,561,560,559,558,557,556,555,554,553,552,551,550,549,548,547,546,545,544,543,542,541,540,539,538,537,536,535,534,533,532,531,530,529,528,527,526,525,524,523,522,521,520,519,518,517,516,515,514,513,512,511,510,509,508,507,506,505,504,503,502,501,500,499,498,497,496,495,494,493,492,491,490,489,488,487,486,485,484,483,482,481,480,479,478,477,476,475,474,473,472,471,470,469,468,467,466,465,464,463,462,461,460,459,458,457,456,455,454,453,452,451,450,449,448,447,446,445,444,443,442,441,440,439,438,437,436,435,434,433,432,431,430,429,428,427,426,425,424,423,422,421,420,419,418,417,416,415,414,413,412,411,410,409,408,407,406,405,404,403,402,401,400,399,398,397,396,395,394,393,392,391,390,389,388,387,386,385,384,383,382,381,380,379,378,377,376,375,374,373,372,371,370,369,368,367,366,365,364,363,362,361,360,359,358,357,356,355,354,353,352,351,350,349,348,347,346,345,344,343,342,341,340,339,338,337,336,335,334,333,332,331,330,329,328,327,326,325,324,323,322,321,320,319,318,317,316,315,314,313,312,311,310,309,308,307,306,305,304,303,302,301,300,299,298,297,296,295,294,293,292,291,290,289,288,287,286,285,284,283,282,281,280,279,278,277,276,275,274,273,272,271,270,269,268,267,266,265,264,263,262,261,260,259,258,257,256,255,254,253,252,251,250,249,248,247,246,245,244,243,242,241,240,239,238,237,236,235,234,233,232,231,230,229,228,227,226,225,224,223,222,221,220,219,218,217,216,215,214,213,212,211,210,209,208,207,206,205,204,203,202,201,200,199,198,197,196,195,194,193,192,191,190,189,188,187,186,185,184,183,182,181,180,179,178,177,176,175,174,173,172,171,170,169,168,167,166,165,164,163,162,161,160,159,158,157,156,155,154,153,152,151,150,149,148,147,146,145,144,143,142,141,140,139,138,137,136,135,134,133,132,131,130,129,128,127,126,125,124,123,122,121,120,119,118,117,116,115,114,113,112,111,110,109,108,107,106,105,104,103,102,101,100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-96,-97,-98,-99,-100,-101,-102,-103,-104,-105,-106,-107,-108,-109,-110,-111,-112,-113,-114,-115,-116,-117,-118,-119,-120,-121,-122,-123,-124,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-135,-136,-137,-138,-139,-140,-141,-142,-143,-144,-145,-146,-147,-148,-149,-150,-151,-152,-153,-154,-155,-156,-157,-158,-159,-160,-161,-162,-163,-164,-165,-166,-167,-168,-169,-170,-171,-172,-173,-174,-175,-176,-177,-178,-179,-180,-181,-182,-183,-184,-185,-186,-187,-188,-189,-190,-191,-192,-193,-194,-195,-196,-197,-198,-199,-200,-201,-202,-203,-204,-205,-206,-207,-208,-209,-210,-211,-212,-213,-214,-215,-216,-217,-218,-219,-220,-221,-222,-223,-224,-225,-226,-227,-228,-229,-230,-231,-232,-233,-234,-235,-236,-237,-238,-239,-240,-241,-242,-243,-244,-245,-246,-247,-248,-249,-250,-251,-252,-253,-254,-255,-256,-257,-258,-259,-260,-261,-262,-263,-264,-265,-266,-267,-268,-269,-270,-271,-272,-273,-274,-275,-276,-277,-278,-279,-280,-281,-282,-283,-284,-285,-286,-287,-288,-289,-290,-291,-292,-293,-294,-295,-296,-297,-298,-299,-300,-301,-302,-303,-304,-305,-306,-307,-308,-309,-310,-311,-312,-313,-314,-315,-316,-317,-318,-319,-320,-321,-322,-323,-324,-325,-326,-327,-328,-329,-330,-331,-332,-333,-334,-335,-336,-337,-338,-339,-340,-341,-342,-343,-344,-345,-346,-347,-348,-349,-350,-351,-352,-353,-354,-355,-356,-357,-358,-359,-360,-361,-362,-363,-364,-365,-366,-367,-368,-369,-370,-371,-372,-373,-374,-375,-376,-377,-378,-379,-380,-381,-382,-383,-384,-385,-386,-387,-388,-389,-390,-391,-392,-393,-394,-395,-396,-397,-398,-399,-400,-401,-402,-403,-404,-405,-406,-407,-408,-409,-410,-411,-412,-413,-414,-415,-416,-417,-418,-419,-420,-421,-422,-423,-424,-425,-426,-427,-428,-429,-430,-431,-432,-433,-434,-435,-436,-437,-438,-439,-440,-441,-442,-443,-444,-445,-446,-447,-448,-449,-450,-451,-452,-453,-454,-455,-456,-457,-458,-459,-460,-461,-462,-463,-464,-465,-466,-467,-468,-469,-470,-471,-472,-473,-474,-475,-476,-477,-478,-479,-480,-481,-482,-483,-484,-485,-486,-487,-488,-489,-490,-491,-492,-493,-494,-495,-496,-497,-498,-499,368,367,366,365,364,363,362,361,360,359,358,357,356,355,354,353,352,351,350,349,348,347,346,345,344,343,342,341,340,339,338,337,336,335,334,333,332,331,330,329,328,327,326,325,324,323,322,321,320,319,318,317,316,315,314,313,312,311,310,309,308,307,306,305,304,303,302,301,300,299,298,297,296,295,294,293,292,291,290,289,288,287,286,285,284,283,282,281,280,279,278,277,276,275,274,273,272,271,270,269,268,267,266,265,264,263,262,261,260,259,258,257,256,255,254,253,252,251,250,249,248,247,246,245,244,243,242,241,240,239,238,237,236,-95,-96,-97,-98,-99,-100,-101,-102,-103,-104,-105,-106,-107,-108,-109,-110,-111,-112,-113,-114,-115,-116,-117,-118,-119,-120,-121,-122,-123,-124,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-135,-136,-137,-138,-139,-140,-141,-142,-143,-144,-145,-146,-147,-148,-149,-150,-151,-152,-153,-154,-155,-156,-157,-158,-159,-160,-161,-162,-163,-164,-165,-166,-167,-168,-169,-170,-171,-172,-173,-174,-175,-176,-177,-178,-179,-180,-181,-182,-183,-184,-185,-186,-187,-188,-189,-190,-191,-192,-193,-194,-195,-196,-197,-198,-199,-200,-95,-96,-97,-98,-99,-100,-101,-102,-103,-104,-105,-106,-107,-108,-109,-110,-111,-112,-113,-114,-115,-116,-117,-118,-119,-120,-121,-122,-123,-124,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-135,-136,-137,-138,-139,-140,-141,-142,-143,-144,-145,-146,-147,-148,-149,-150,-151,-152,-153,-154,-155,-156,-157,-158,-159,-160,-161,-162,-163,-164,-165,-166,-167,-168,-169,-170,-171,-172,-173,-174,-175,-176,-177,-178,-179,-180,-181,-182,-183,-184,-185,-186,-187,-188,-189,-190,-191,-192,-193,-194,-195,-196,-197,-198,-199,-200])
    assert Solution().arrayRankTransform([-752568125,-755503750,-758439375,-761375000,-764310625,-767246250,-770181875,-773117500,-776053125,-778988750,-781924375,-784860000,-787795625,-790731250,-793666875,-796602500,-799538125,-802473750,-805409375,-808345000,-811280625,-814216250,-817151875,-820087500,-823023125,-825958750,-828894375,-831830000,-834765625,-837701250,-840636875,-843572500,-846508125,-849443750,-852379375,-855315000,-858250625,-861186250,-864121875,-867057500,-869993125,-872928750,-875864375,-878800000,-881735625,-884671250,-887606875,-890542500,-893478125,-896413750,-899349375,-902285000,-905220625,-908156250,-911091875,-914027500,-916963125,-919898750,-922834375,-925770000,-928705625,-931641250,-934576875,-937512500,-940448125,-943383750,-946319375,-949255000,-952190625,-955126250,-958061875,-960997500,-963933125,-966868750,-969804375,-972740000,-975675625,-978611250,-981546875,-984482500,-987418125,-990353750,-993289375,-996225000,1000000000,997064375,994128750,991193125,988257500,985321875,982386250,979450625,976515000,973579375,970643750,967708125,964772500,961836875,958901250,955965625,953030000,950094375,947158750,944223125,941287500,938351875,935416250,932480625,929545000,926609375,923673750,920738125,917802500,914866875,911931250,908995625,906060000,903124375,900188750,897253125,894317500,891381875,888446250,885510625,882575000,879639375,876703750,873768125,870832500,867896875,864961250,862025625,859090000,856154375,853218750,850283125,847347500,844411875,841476250,838540625,835605000,832669375,829733750,826798125,823862500,820926875,817991250,815055625,812120000,809184375,806248750,803313125,800377500,797441875,794506250,791570625,788635000,785699375,782763750,779828125,776892500,773956875,771021250,768085625,765150000,762214375,759278750,756343125,753407500,750471875,747536250,744600625,741665000,738729375,735793750,732858125,729922500,726986875,724051250,721115625,718180000,715244375,712308750,709373125,706437500,703501875,700566250,697630625,694695000,691759375,688823750,685888125,682952500,680016875,677081250,674145625,671210000,668274375,665338750,662403125,659467500,656531875,653596250,650660625,647725000,644789375,641853750,638918125,635982500,633046875,630111250,627175625,624240000,621304375,618368750,615433125,612497500,609561875,606626250,603690625,600755000,597819375,594883750,591948125,589012500,586076875,583141250,580205625,577270000,574334375,571398750,568463125,565527500,562591875,559656250,556720625,553785000,550849375,547913750,544978125,542042500,539106875,536171250,533235625,530300000,527364375,524428750,521493125,518557500,515621875,512686250,509750625,506815000,503879375,500943750,498008125,495072500,492136875,489201250,486265625,483330000,480394375,477458750,474523125,471587500,468651875,465716250,462780625,459845000,456909375,453973750,451038125,448102500,445166875,442231250,439295625,436360000,433424375,430488750,427553125,424617500,421681875,418746250,415810625,412875000,409939375,407003750,404068125,401132500,398196875,395261250,392325625,389390000,386454375,383518750,380583125,377647500,374711875,371776250,368840625,365905000,362969375,360033750,357098125,354162500,351226875,348291250,345355625,342420000,339484375,336548750,333613125,330677500,327741875,324806250,321870625,318935000,315999375,313063750,310128125,307192500,304256875,301321250,298385625,295450000,292514375,289578750,286643125,283707500,280771875,277836250,274900625,271965000,269029375,266093750,263158125,260222500,257286875,254351250,251415625,248480000,245544375,242608750,239673125,236737500,233801875,230866250,227930625,224995000,222059375,219123750,216188125,213252500,210316875,207381250,204445625,201510000,198574375,195638750,192703125,189767500,186831875,183896250,180960625,178025000,175089375,172153750,169218125,166282500,163346875,160411250,157475625,154540000,151604375,148668750,145733125,142797500,139861875,136926250,133990625,131055000,128119375,125183750,122248125,119312500,116376875,113441250,110505625,107570000,104634375,101698750,98763125,95827500,92891875,89956250,87020625,84085000,81149375,78213750,75278125,72342500,69406875,66471250,63535625,60600000,57664375,54728750,51793125,48857500,45921875,42986250,40050625,37115000,34179375,31243750,28308125,25372500,22436875,19501250,16565625,13630000,10694375,7758750,4823125,1887500,-1048125,-3983750,-6919375,-9855000,-12790625,-15726250,-18661875,-21597500,-24533125,-27468750,-30404375,-33340000,-36275625,-39211250,-42146875,-45082500,-48018125,-50953750,-53889375,-56825000,-59760625,-62696250,-65631875,-68567500,-71503125,-74438750,-77374375,-80310000,-83245625,-86181250,-89116875,-92052500,-94988125,-97923750,-100859375,-103795000,-106730625,-109666250,-112601875,-115537500,-118473125,-121408750,-124344375,-127280000,-130215625,-133151250,-136086875,-139022500,-141958125,-144893750,-147829375,-150765000,-153700625,-156636250,-159571875,-162507500,-165443125,-168378750,-171314375,-174250000,-177185625,-180121250,-183056875,-185992500,-188928125,-191863750,-194799375,-197735000,-200670625,-203606250,-206541875,-209477500,-212413125,-215348750,-218284375,-221220000,-224155625,-227091250,-230026875,-232962500,-235898125,-238833750,-241769375,-244705000,-247640625,-250576250,-253511875,-256447500,-259383125,-262318750,-265254375,-268190000,-271125625,-274061250,-276996875,-279932500,-282868125,-285803750,-288739375,-291675000,-294610625,-297546250,-300481875,-303417500,-306353125,-309288750,-312224375,-315160000,-318095625,-321031250,-323966875,-326902500,-329838125,-332773750,-335709375,-338645000,-341580625,-344516250,-347451875,-350387500,-353323125,-356258750,-359194375,-362130000,-365065625,-368001250,-370936875,-373872500,-376808125,-379743750,-382679375,-385615000,-388550625,-391486250,-394421875,-397357500,-400293125,-403228750,-406164375,-409100000,-412035625,-414971250,-417906875,-420842500,-423778125,-426713750,-429649375,-432585000,-435520625,-438456250,-441391875,-444327500,-447263125,-450198750,-453134375,-456070000,-459005625,-461941250,-464876875,-467812500,-470748125,-473683750,-476619375,-479555000,-482490625,-485426250,-488361875,-491297500,-494233125,-497168750,-500104375,-503040000,-505975625,-508911250,-511846875,-514782500,-517718125,-520653750,-523589375,-526525000,-529460625,-532396250,-535331875,-538267500,-541203125,-544138750,-547074375,-550010000,-552945625,-555881250,-558816875,-561752500,-564688125,-567623750,-570559375,-573495000,-576430625,-579366250,-582301875,-585237500,-588173125,-591108750,-594044375,-596980000,-599915625,-602851250,-605786875,-608722500,-611658125,-614593750,-617529375,-620465000,-623400625,-626336250,-629271875,-632207500,-635143125,-638078750,-641014375,-643950000,-646885625,-649821250,-652756875,-655692500,-658628125,-661563750,-664499375,-667435000,-670370625,-673306250,-676241875,-679177500,-682113125,-685048750,-687984375,-690920000,-693855625,-696791250,-699726875,-702662500,-705598125,-708533750,-711469375,-714405000,-717340625,-720276250,-723211875,-726147500,-729083125,-732018750,-734954375,-737890000,-740825625,-743761250,-746696875,-749632500,-752568125,-755503750,-758439375,-761375000,-764310625,-767246250,-770181875,-773117500,-776053125,-778988750,-781924375,-784860000,-787795625,-790731250,-793666875,-796602500,-799538125,-802473750,-805409375,-808345000,-811280625,-814216250,-817151875,-820087500,-823023125,-825958750,-828894375,-831830000,-834765625,-837701250,-840636875,-843572500,-846508125,-849443750,-852379375,-855315000,-858250625,-861186250,-864121875,-867057500,-869993125,-872928750,-875864375,-878800000,-881735625,-884671250,-887606875,-890542500,-893478125,-896413750,-899349375,-902285000,-905220625,-908156250,-911091875,-914027500,-916963125,-919898750,-922834375,-925770000,-928705625,-931641250,-934576875,-937512500,-940448125,-943383750,-946319375,-949255000,-952190625,-955126250,-958061875,-960997500,-963933125,-966868750,-969804375,-972740000,-975675625,-978611250,-981546875,-984482500,-987418125,-990353750,-993289375,-996225000,-999160625]) == [85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 682, 681, 680, 679, 678, 677, 676, 675, 674, 673, 672, 671, 670, 669, 668, 667, 666, 665, 664, 663, 662, 661, 660, 659, 658, 657, 656, 655, 654, 653, 652, 651, 650, 649, 648, 647, 646, 645, 644, 643, 642, 641, 640, 639, 638, 637, 636, 635, 634, 633, 632, 631, 630, 629, 628, 627, 626, 625, 624, 623, 622, 621, 620, 619, 618, 617, 616, 615, 614, 613, 612, 611, 610, 609, 608, 607, 606, 605, 604, 603, 602, 601, 600, 599, 598, 597, 596, 595, 594, 593, 592, 591, 590, 589, 588, 587, 586, 585, 584, 583, 582, 581, 580, 579, 578, 577, 576, 575, 574, 573, 572, 571, 570, 569, 568, 567, 566, 565, 564, 563, 562, 561, 560, 559, 558, 557, 556, 555, 554, 553, 552, 551, 550, 549, 548, 547, 546, 545, 544, 543, 542, 541, 540, 539, 538, 537, 536, 535, 534, 533, 532, 531, 530, 529, 528, 527, 526, 525, 524, 523, 522, 521, 520, 519, 518, 517, 516, 515, 514, 513, 512, 511, 510, 509, 508, 507, 506, 505, 504, 503, 502, 501, 500, 499, 498, 497, 496, 495, 494, 493, 492, 491, 490, 489, 488, 487, 486, 485, 484, 483, 482, 481, 480, 479, 478, 477, 476, 475, 474, 473, 472, 471, 470, 469, 468, 467, 466, 465, 464, 463, 462, 461, 460, 459, 458, 457, 456, 455, 454, 453, 452, 451, 450, 449, 448, 447, 446, 445, 444, 443, 442, 441, 440, 439, 438, 437, 436, 435, 434, 433, 432, 431, 430, 429, 428, 427, 426, 425, 424, 423, 422, 421, 420, 419, 418, 417, 416, 415, 414, 413, 412, 411, 410, 409, 408, 407, 406, 405, 404, 403, 402, 401, 400, 399, 398, 397, 396, 395, 394, 393, 392, 391, 390, 389, 388, 387, 386, 385, 384, 383, 382, 381, 380, 379, 378, 377, 376, 375, 374, 373, 372, 371, 370, 369, 368, 367, 366, 365, 364, 363, 362, 361, 360, 359, 358, 357, 356, 355, 354, 353, 352, 351, 350, 349, 348, 347, 346, 345, 344, 343, 342, 341, 340, 339, 338, 337, 336, 335, 334, 333, 332, 331, 330, 329, 328, 327, 326, 325, 324, 323, 322, 321, 320, 319, 318, 317, 316, 315, 314, 313, 312, 311, 310, 309, 308, 307, 306, 305, 304, 303, 302, 301, 300, 299, 298, 297, 296, 295, 294, 293, 292, 291, 290, 289, 288, 287, 286, 285, 284, 283, 282, 281, 280, 279, 278, 277, 276, 275, 274, 273, 272, 271, 270, 269, 268, 267, 266, 265, 264, 263, 262, 261, 260, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 247, 246, 245, 244, 243, 242, 241, 240, 239, 238, 237, 236, 235, 234, 233, 232, 231, 230, 229, 228, 227, 226, 225, 224, 223, 222, 221, 220, 219, 218, 217, 216, 215, 214, 213, 212, 211, 210, 209, 208, 207, 206, 205, 204, 203, 202, 201, 200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181, 180, 179, 178, 177, 176, 175, 174, 173, 172, 171, 170, 169, 168, 167, 166, 165, 164, 163, 162, 161, 160, 159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144, 143, 142, 141, 140, 139, 138, 137, 136, 135, 134, 133, 132, 131, 130, 129, 128, 127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert Solution().arrayRankTransform([]) == []
    assert Solution().arrayRankTransform([-1000000000,-1000000000,-1000000000,1000000000,1000000000,1000000000]) == [1, 1, 1, 2, 2, 2] 
    assert Solution().arrayRankTransform([0,0,0,-1]) == [2, 2, 2, 1]
    
    print('All passed')

