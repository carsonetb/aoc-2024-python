import copy

data = """SXMAXXMSSSMMXAMXAMXMMXXXAXMAAMAXXAMXMMAMXMASXMASXXSMMMAXXAMXAMASXMSMMMAASMSMMMXMASAXMAXAMXSAXXMXXMXSXMXAMXMXSSMXAMXSXMMSMMSMSASXXMXMMMXMMMMM
SAMXSMXMAAAASMSMXSXAXASMSSMSSSXSSSMMSASMXMAMMXMASXMMXSAMMSMAMSAMAMXSAXMMXAAXAMAXSAMXMSXSXMXSAAXAXSMMAMSMSXSASAAMSSMMAMXXAAXXAAAMASMMASAMAAAX
MAMMAXSMSMMMXAAMAMMSMASAAAXAMXAXAAAAXMAMAMMMSAMMAXXAAMASAAXXAMASXMASMMMASXMSMSXXAMXSSMAXAAAXXXMXXMAMAMAASAMXXMSMMAXSAMASMMSAMXMSAMASASASMXMS
SSMMMAXAAXSAMSMMASAAMAMMMMMMSMMMSMMMSXMSMSXXMASXMSMSMSAMXXMXMAXMXSXSXSMASAAXMAXXXXAMAMSMAMMSXSMMASXMAMMXMMMSSXMASAMMASASAAXXXAXMASAMXMAMAASM
AAXAMXMSMMMXMXAMXMXSMMXSXMAXAXXAXXXAAAMAASMMSXMMXAAXAMXAASMXXSAMXMAMAAMXMXMXMAXMMMMSMMAXMAMMMAASAMAXMXSXMXAAXASAMASAXAMXMXMMXXSSMMMXAMXMSMMA
MMSXMAAXMSMMAMAAXAAMASMMASXXXXXSSMMXSMMMSMAXSASXSMSMMSSMXSAASMMMMMAMMMSSMSXXMMSMAAMAXMMSASAAXSMMASMMMAAAAMMSSMMAXSMMXAXAMMSMSSMAMAMMSMSMXMMS
XXSASMSXXASXXMXMMMMSMMAMMMMSAMSAMXAMXXAXMMSMSAMAXXXASAMXSMMMXAAAAMMSMAMAASAMXAAXSSSXSAXAAMXAMXXMAXAAMAXMMSAMXXMXSXXSSSMMSAAASXSAMXMAXSMAMMAA
MMSMMMMMSAXMMAAXAMXMMAXMAAAMAMAASASMSSMXSAMXMAMSMXSSMMSXMAMASMMSSMMAMMSMMMMSSSXMMMMAMMXMSMSSSMSMASXMSSSMASAXXSAMXMAXXAXXAMMXMXSXSSMMSAMXMMMM
AMSXXAAMMSMAAXSSXSAAXAMXMMMXSAMXXAXAMASAMXMSSMXXXMMXSXAMMAMMMAAAAASAMAAAMSMAAMXSAAMSMAAXAMMXAAMXMAAXAMAMASMSAXXMAMAMSMMXXXMASXXMAXAMXMMMMASM
SXSASMSXAXMSSXMAXSMSMAXMAXXSMMXSMMMMSMMXSAXXAMAMSMSAMXMSSMSSSMMMSMMAMSMSASMMMMASMMSAMSSSMSSSMMMASMSMXMXMMSASMMMSMSAASXSMMASASMMSMXSMSMAMSASA
MAXMSAXMMMMAXAMSMMAXXAMSMSMSASAMXAAAAMXMMMXXAMXXXAAASMMAAAAAMSMMXMMSMMAMMMMSAMMSXMAMXAAXAAAXXAMXSAAXAMSSMMXXAAASAXMXXAAASAMAXMAAAXMAMSAMMASM
MXMXMMMXMAMMXAMXAMMMMXXAAAAXAMXSSMSSXXAAAMAMSXSMMSMSAXMSMMMSMSXMASMXXMAMXAAXMXXXAMMXMMSMMMSMSXXSMXMSMXAAXXMSMMXMAMMSXSSXMXSSSMSXMAMAMSMXMMXX
MMXXSAMASXSSXSXSXMMAMASMSMSMXMXXAAMAMMSSMMSSMAAXAXMMXXXAMXAMMSASAMXMMXSXSMSSSSSSMMXAMXAMAXAAMXXSASXSMMSSMAMAAMMMXMAAMXAMXXXAMXMMSSSMMXSXAXMM
XXMASASXSAMXXMAXXMMAMMMAAAAXAASMMMMAMXXAAXMAMSMMMMXAAXMMMMMSASAMXSAXXAMAMXXAAAXAAMSMMSASMSSSSMAMAMAXMAAAXMSMXSAMXMXSSMAMASMASMXMAXAASASMMMAM
SMAAMAMXSMMMMMAMSXSMSAMXMSMSXSAAXAMAXAXMMMXAMXXXSMMXSXSAXSAMAMSMASAMAMSAMXMMMMSSMMAAMSMMAAMMXAAMAMXMMXSSMMXAASAMMMMXAMMMAXMXAXAMMSMMMXXASASA
AASMSSSXXXAAMMMSMAAASAMXMAMAMXMXSSSSSXMAASXMXMXMXASXMAMXSMAMXMXMASAAXMAMXAAXAXAMXSMSMSAMMMXMMXMSMMSASAAMXMMMMMASXAMSSMMMSSXMASMMXAMASXSMMAMX
MMXMAMXAXSSSSXMAMXAAMMSXMXMMAXMMXMAXAASXMSASXSAAXMMAMXMMMXAMASXMXSXSSXASXSSSMMMSAXAMASXMMSSMMSAXAMXAMMSMMMXAASMMMAXAMXSAAMAXXSXSXMMMSAAAMAMX
XMMMXSMSMAAAMXSXSSMSMXMAMXSSMAMAAMMMSMMAMMAMASXMXASMMMMAASXMXXAMMMMAMAXXXMAMMSAMAMXMAMASAAAASMXMASMXMXAXXSSMMSAASMMXXAMMSSMMXMASASXMMXMMMASM
AMASMMAMMMMMMMMAMAAAXAMAMAMAXAASMMSAMXSAMMAMXMASAMXASXSMMAAMSSMMAMSAMXMSAMXMXMMSMMSMMSAMMXMMMAXMASXXMSMSXMASAXMMMAMSMAXAMXMAMXASAMAXAMXAXXXA
XAMXAMAMAMASAMMAMMMMSASMMXSSSMXAMXMMSASXSSSXSAMAAXAAXAAXSMSMAAMSMMMXMASXMMXMAXXMXAXAXMASASXXSXSMASMSAAAMMMMMXMAAXAASXXMXSAXMAXXXASAMXSSMSMSM
MXXSXMXSXSASASXMMSAMMXAAXAMXAMSMSMSXMAMAMAMMSAMASXSSMAMMXXMMSXMAAAMMSMSASAAMMMMSMMSMMSXMASAASAXMXSASMMAMSXSAMXMMSMASASASMMSXSSSSXMAMMMMMAAAX
ASMMXSAMXMASAMMMAXAXMXSXMXMSAMAAMAMXMAMMMAMASAMAXAMXAAAMXSMAXASXMXMAAAXAMSXMAASAAAMAAMXMAMMMMAMMMMAMAXMAMAMAMAAAXMAMAAMXAASMAAAXXSAMAXAMMXMX
MXAAASXMAMMMMAAMMMSMMAMSMAMMMMMAMAMXXMSXMSMAXXMAXAMAXMAXAXMASXMSAAMSMSMAMAMMSMSASAMMSSXMSSMAXMMAMMSMSMXAMMMAMSMMXXSMSMMSMMSAMMMMMSXSSXSMXSSM
XSMMXSXSASMMSSXSXAMSMXSAMASAMSXSSMMSAMMMMXMMMXMMXAMSSSXMSSMMXXAMMMMAAXMAMAMAMASXMAXAXXXMAAMXMASXMXMAXMMASMMXXMASMXXAMXMAXXXXMMMSXMASXMMSMAXA
XXXMAMASASXAXMAMMMMAMMXMSAXASAAAXAASAMAMXSASMSASXSXMAMAXMAMXAMSMMAMMXMAMSAXXSAMMSXMMSXSMSSMSMAAAASMMMSMASXSAASAMAAMMMSSMSAMXSXMXAMMSAMAAMMMS
SASMASAMXSMSMAASMXSAMXAXMXSMMMMMMMMSAMXSAMSAAMASMMAMSMMXSAMMMXAAMAMMXMXXMMSMMASXMAMMMAXAAAAMMAMXMSAAAAMXMAXMMMXAMXSAAMAMXXSAMXXSXMXMAMSXXMAM
AAXSASXSXXAAXSMSXAMXSXMMAAMAAXAXAMAMASAMXMMMXMAMMSAMAAMMSXMAMXXMMSAMAXASXAAASAMAXXMAMSMSMMSMMASAAXMMSMSAMXMXXASXSMSMMSAMMXMAMXASMMASAMASMMSX
MMMMMSAMMMMMXMAXMMMXMMSMMASXMSMSXMASXMASMSSMAMMSASAMMXMAMMSASXSXAXASXSAMMSMMMMSSMSSMMXAMSMMASASMSMXMAMXAXAMXMMSAAASXMSAXSAXMSSMXASAXAXAXMAMS
XASAAMAMMAMSXMAMAASMSAXAMASXMAMSMMAXASXMAAASMSXMMMXMASMMXAMAMMAMXSAMXMXMAMSMSMAMXAAAXMAMMXSMMMSAMXSMMMMMSSSXMAMXMMMAXSXMXXSXXAXMXMMSSMMSMAMS
SXSAMSXMSSSMAXSSSXSAMMSSMAXASMMSAMSSMMMMMSXMXAXMSSMMMAAXMXMXMSAMMMAAXMAMSXAXAMASMSSMMSXMAASAXXMAMMXAAAXMAMXXMASAXAXMMMMSMMMXMXMXAAAAAMAXMMXX
SMMXXSAMXMAMXMMAXAMXMXMAMAXMMSAMMMAAXMAAAMASMMMAAXAAXMAMSMSSMSASXSSMXSMSMXMMXMAXXMAMXXAMMMSAMMXMXMSSMMMAASXXSXXMXXSMSMAAAMASMSMSMSXMASMXXSSM
MAAMMMASASAMXMMMMXMAXXSMSSSMAMSMXMSSMASMMSAMAXMMSSSMSMMAXAXMAXAMXMASAMXAXAMSAMAMSSMMXSMMSMXAMSAMAXMAMSASMSMMMSMMSMSAAMMSSMAMMAAAAAAXAAAXAAAA
SMMXASMMAMXXAXAXMXSMSXSXAAAMAMMSMXAAXAAAXMXSSXAAAAAAXASMMMMSSMMMAXSMSSMMSMAAAMAMXAAXMASASASMMXASXSSSMMMMAMXAASXMAAMSMMXMXMMSSMSMSMXMASMMMAMS
SASXXSAMMMMSMSXSXAAXMAMMMXMMMMMAMMMSMMXXMSXMMASMMSMXMAMXAAAAXAASMSXAAXAXXMAXXSXSXSXMAMMMSMXSASXMAXMAAAXMAMXMXXAMMSMMMSAMMSMAAMMMXMAMXMXMMAXX
SAMXXXAMAAXAMSMMMSSMMAMAAXMXMASAMSAMXSMSAXMAAXMAMXXMASMSMMMSXMMAXSMMMSSMXMSSMSAMAXASXSAXXXASXMASMMSSMMMSAMASMSSMXXMAASASAAMSXMMMAXMSMXXMAXSM
MAMMASXSSXSXXXAAMMAMSASMSMMASAMAAMXSMAAMMMSSMSSXMXXMAMMASAXMXSMSMSSMAAAMXAAAMXAXMAMSASXSXMAXAMXMSAMXMAXXMAMXAAAMMSXMXSXMMSMMXAASMMSAXMMSSXAM
SAMMAAMAMAAXSSSMMMAMAAMAAASMMSSMMMAXAMXMXAAXMAMAASXMAMSASXSMMSAAXMMSMSAMMAMXMSMMSSMMMMMMAMSSSMSAMXSASXSASMXMMMXAAXASAMASXMAMSSMXXMXAXXAAAMXM
SXXMMXMAMMMMMAMMXSMMMMMMMXMSAAXXAMSSSXXSXMASXASMMAAMXMMASAXMAMSMMMAXMMAXSXSSXMXAAMXMAAAMXMAAAMMMAXXXMAMAXMASMSSSSSMMASAMAMXMMASXAMMSMMMMSASX
SXXXMXMXSAAAMAMAXSAAAASAMSAMMMMMXSMAMXMAXMAMMMSASMSMXXMXMMMMAXMMMMAXXMSMXAXXAMMMMSASXSSSXSMSAMAMAMMAMXMMMMXMAMAMXAXMMMMSSMMMSAMXAMAMAXSAXMMM
SXMASAMMSXSSSSSXMSMMMMMASMXMSASMSSMAMMAMMMASAMXAMAAXMXMAMXAMXXMAAXXSSXMMMMMSSMMAXSXSAAAXAXMXMXAMAXSASXSSSMSMMMMMMAMAAAXXXAMXMMMSSMASAMSAMXAM
XAMAAASXMAMAAAAXXMSMXSMMMAMXSASXAXXAXAMXXSASXSMSMSMMMMSAMSXSSSSSMSAAAMAAMSXMAMMMXSAMMMXMMMMASMSSSXMASAAAAAXXXAAMSXMSXXMAMXMAMSAMXSASXMMAMSSS
MXMXXSMAMSMMMMMMSMAMAMASMSMAMAMMMSSMXSAMXMASAMAAAAMAAMXSMSAMAAAAAAMMMSSXXSMMAMASAMAMAMAXMAMXMSAAMXMXMMMSMSMMSSSMSAAXASMSMSMAAMAXAMXSAMMMMXAX
MAXXSAMSMMASXMSAMXAMAMMMAAMXMAMMXMASAXAMAMAMAMSMSMSSXXAMXMAMMMMMMMSXXAMMMSASASAMXXAXASASMMSSSXMSMSSSXXMXAXXAMAAAMMMMAMAASAMXXSSMSSMSXMASMAMS
SSSMAAAXASAMAAMSXSSSMSSMXMSMSSMSASXMMSMSMXAMXMXAAAXAAMSMASXMAMXSSXMXMAMAAMAMXMASASXSMSMSAMAMXAXMASASAMMMMMASMSMMMAAMAMSMSMSSMAAXMAXMASXSAMXA
SAAASMMMXMAMMXMXMAMAMXAAASAMXAASAMXAAMXSASXSMAMSMSMMMMXAXMAXXSAMMAXAXSSMSSSSXSAMXXXAXMAXAMASMSMMXMAMXAAAMAXAXAMSSSSSXMXAMXAAMSMMSMMSXMAMMSSM
MAMMXMMSMMXXXMXXMMMSMSMMMSASMMMMAXSXMASMAXXAXXXXXMASAMXSAXAMSMASMMMSAMXMMAAAAMXSMSSMMMMMASXSAMMSAMXMASXXSSSSMSXAAMXMMMMSMMSXMAXMAAMMMMAMSAXX
MMXMXXAAAXMAMSMMMAAXMSAAASMMMMASXMAMXXXMAMSXMSMSASASASAMSMSSMAAAAXAMMASMMMMMMMMMAMAAAAXSXMXMXMAXXSASMMSMMMAMAXMMSMAMSMAAXMMXMAMSSXMXAMASMXSS
SXASMMSSSMAAMAAAMMMSASMMMXXSASXSAAAAXMSXSMSMAAAMAMXSAMASAMXAMMMXSMSSMASAAXXSXSXSXXAMMSXSASXSXMXSAMXSAAXMAMAXMMMMAMASAMSSSXMAXSAAMAXSSSSXMXMA
MMMSAAAAMMSMSAXMXAAMAMXSAMXSASASXMXSAAMXMASMSMSMAMAMMMXMXXMAMXSAAAAXMAXMMMMMASAMASMMMXXMASAMXXMAMMMSMMSXMSMMAAXSASXMAMXXMASXSMMASMMAXXXASMSS
XAXXMMMXMXAXXMASXMXSASMXMAMMAMMMXMAXMSMMMXMXXAAXAMASXXXAMXSSMAMXAMXSMXMAAXAMAMAMAMAAMSMMAMXMAMSAASAXMASXAAAASMMMXMAXSMAMMAMXAXMXMXAMXMXSMAXM
XMSMXXXASMMSXSAXAAXMAXXMAXXMMSXMAMMSXXMASXSAMXMMMXAXMMMXSMAAMXSMMMMMAASXMSSMASAMXSXMMAAMXMMASAMMSSMXMASMSMSMXAXXXXSAMMMMSSSMMXAAAXMAXAXMMSMM
SAMXSAAXMAXXAMSSMMSMASMMSSXMASASMSAMMXMXSAMXSMMASMMXSAASMMMMMASAASAMMMMAAXASAXASASMMSSSSMSMAMXSXXMASMMXAMXXXMMSSMAMASAXAAXXAXSSMSMMSMSMXAAXM
ASMAXMASMSMMMMAXXAXMAMAAAMAMXSAMAXAXMAMAMXMMMASAXAXAMXXXXAAXMXXXMSASMSSMMSMMMSMMXXAXAAAXAAMXSAXMXMAMAAMSMMMMMXAAMXMAMMMMXXXSMMXMXXAAAAAMSMSS
MAMMSXXXMAXXAAXSMMXMMMMMMMSMMMXMXSAMSMSAMXMASXMAMSMMMSXMSMSSMMSSMSAXAXXXAAAMXAXAMMSMMMSMSMSAMMMMMMAXMXSXAAAASMSSMAMASXSSSSMMASAMSMXSSMXMAAAA
XMXMAMMXAAXSASXMAXASMSSXSAXXMAXXMXXAAMAASAMXSMASMMASAAAMAMAXAAXXAMMMSMSMSSSMSMSXSXXAAAMAMXMMXAAXMSMSMXAXMMSMSAAAXXSASAXAAAMSAMAASAMMAMSMMMAS
MXSMAMXSXMMSAXASXXXSAAAAMMMMMSMMSMMMMSSMMXSXSXAMMXAMXSSSSMASMMMMMMXAMAMAXAMAMASAMAXSMXSAXMASMSSSMAAAMXSXSXMXMMMSSMMMMXMMSMMMAXMMMAMSAMAXSSMM
MMAMXXAMASAMMMXMSAAMMMMMSSXSAAAAMAMSMAMAMXXAXMASXMMMXMMAMMAXAMASXMMSSSMSMSMAMXMAMAMMXAMMMAXXMAAAMAMASMMAMXMASAMAAASXMMSXMAXMAMSASAMXXMAXXAAA
XSSMSMASAMMSAMAAXMXMAXAXAAAMMXSMMAMAMASAMMMSMMAMAMXSXSMMMMSMSAMXAXAAXAAXAMSMSXSXMXSMAMMSMMMSMMMMMXSASAMXMASMMAMXSXMMSAAMSMMSMXMASASMXMXMSSMM
MMAAXSAMXSASASMAMMSSXSMSMMMMXAMASXSMSXSXSXAAAMMSAMXAASAMSXMAMAMSMMSSMMMMSMAXMAXAMMMXXXAAAAXAAMMSAMMXSXMXXAXXSXMAMAMASMMXAMXSXSMXMAXXAXAAXAAS
ASMMMMXSAMXSXMXMASAMASMMXSXSMASASAAASXSXSMSXSMAXMMSMMMAMXAXMSMMAAMAMAAXSASMMXMMAMAMXMMSSSXSSXMAMAMSASMSMMMXMXAMASAMMXAXSMSXMAMSAMXMSMSSSMXMS
XXASMMMMXSAMAAMSXSXMAMAXSMAXMMMAMMMMMMSAMXXMXMAMSAMXXSXMSMMMAASXSMSSXMXSASXMASMSMXSAAAAXAMXMAMMSSMMASMAAAMASXMMASAMXSXMAXXAMSMXMASMAMAAAMSMM
MSAMAMSMAMAMSSMXMXXMXSXMAMMMSXMXMXXXSAMXMAXMMMXAMXSMXAAMAMAMSMMAXAMXXSASXMXMAMAXSASMSMSXMAXXXMAAMAMMMMSSMSASAAMXSXMXAXXSSSXMAMXMAXXXXMMMMAAA
MXASXMAMXSAAMAASMSMXMAXMAMXAMXAXMASMXSXAMXSMASMMSMSMXMAMASAXXMSXSAMMMMAXSAXMAMSMMMSXMXMASMSMSMMXSAMSSMXXMMMSXMMMMMMMMMMAXMAMXAAMMSSMSMSMSSSM
MSMMMAMMMSMSXMMMXAXAAAMSSSMAMMXMASXMAMSMSAXXAMAXXAXMMXMSMSXXAMMMMAXSAMXMSXSMSMMAAXMASASXMAMAAMAXMASAXMAMSAMXXMAMAAAAAXAMXXXMASXSAAMAAAAAAXMX
XAAAAAXAXXAAASMMXMSMMSAAAXMSMMMMSMMSAXAMXMAMMSMMMMMXMAXAMXMMSMAXSAMASMMXXASXMASXMXSAMXSAMXMMMXMSMXMXMMSSSXASXSASMSMMMAMXMXXSAXAXMXMXXSMMMSXM
XXXMXMMXSMSSMMASXXXMAMMAMSAMXAAMAAAMMMXMAXAMAAAAXAAXXMSASMSAMSMMMASAMXSAMXMAMAMXSAMXSXSXMAMASAMXMAAAMXMMXMAXXSASAMASMMXAAAASAMXMXMSSMMMXAMAM
ASXSAMMAMXAAXSASAMXMXXXAXXMMMSSSSMMXSAMMXXAMSSXMSXMSSXMXMAMAXMSAMXAAXMAXMMMMMSSXMASMSAMXMXSASASASMSMSAAMMSMMXMXMAMXAASXMMSMMAMASXAASAAAMMSAM
XAAXASAMMASXMMSSXSMMASMMXSAXAMAXXAXAMAXASXSMMMMMMXMAMXSAMXMMMXSXSSMMSXMXSXMAAXMXSXMAMAMAMXMAMMMASXXASXSMAAAMAMXMXMMMXMAAXMAMXSASMSAMMMMSAMAX
SSSMAMMXMXMXMXMMAAASASAAAAASXMMMSXMMSSMMSAAXAXXMAAMAMAMASAMASMSAXMAMSXSAMASMMSAAAMSXSAMMMAXMXSMMMMMXMMMMMSMMAXXAAXSXSSXMMSMSXMMSMMXXSXMMMSSM
AAAMXMXSXAXXXSAMSMXMMSMMMMMMAAXXMASXAMAXMXMXSXXMXSSSSSSXMASASASXMSSMMAMMMAMMMMMMSMAMSMSMSMSMAMAAAXMAXAXXXAXSXMXSMSXAAXXSAMXSAMASXMAMSAMAXAAX
MSMMXMASMMMSMMAMMXMMAMXSXSMXSMMSMMAMXSMMMMMXXMMSXAAAXAAAXXAAMAMXXAAAMXMAMXSXXAASAMMMXXAMAAAMMMSSSSMMSMMMMMMMAMXMMXMXMMXMASASXMASASAMSAMAMSSM
XAXSMMAXAAXAASMMMAMMASXXAASAMXXAXSAMXSMAAAMMXAASMMMMMXMMMMMMMSMMMSSMMXMXXXAMSSMSASXAMMSSMSMXSAXXMAMXAAASASASAMAXMAXXAMXSAMMSMMXSMXAMXXMXMMXA
XMXMAMMSSMXMMMAASAMXASAMXMASXSSMXSASAMSSXMSAMMMSASXXXAXAXAAAXXMAXAMAAXAAMSAMAXMSMMMMSAAAAXAAMXMXSSMSMSMSASXSXSAXXASMMMMMXSASAMAMMSMMMMMXMSSM
MSSSSMMAAMXSXSXMSMSMMXMMSXMAXMAMASMMAMXMAAAXMAAXAMMSSMSMSSSSSSSMSASXMXMMXAAMXSMXAMXAMMXMMMMMSMMXAAASAXAMMMAMAMMSMMSAXXXAAMASXMASAAAAAAXSMXAM
MAAAAAMSMMAMAXSXMASMMSAXAMXSASAMMSXSXMAMMMMASXMMAMAXXAAAMAAAAXXXSAMMAMXSXMXMXMASXMMMSMMSXSMAMAMAMMMMAAMMAMAMAMASAMSAMXMASMMMMXAMMSXSSXMXMSXM
MSSMXMAMXMASAMSXMAMAAXMMMMAMXSASASXSXMMMMXXASAMSXMMMMSMSMMMMMMMXMXMAXAMMMSAMXMMMMAMASAMMASMMSSMSAMXSSMXSASXMMXXXAMSASXSAMXSAMMSXXXAAAASAXMAS
MAAXXMASMSASAXSMMSSMSSXAXMAXASAMASAMMMSASAMXMAMAAMMAAXMXXMXMAMMAMMXMAMAAAASAMXXMSMMMSAMMAMXAAXAASMMMAAXMAMMXSMMSAMSAMASXSMMXSAMXAMMMSXMAXXXS
MXSMXMXAXMASMMSAMAAAAXMSXMASMMMMMMAMSASXSXMASAMXXXASASMSXMAMAAMASAAXMXSASMXMMSMMAMAAMXMMAMMMMSMMXSMXMMMSASXMSAAXXMMXMXMASAMXMAXMMMMXMMMSMMAS
SSXMXSAMXXMXMASAMSMMMMMMASMAXASAXMSAMXSAMAMXMAXAMSAMAMXAXSASMXXAXXAMMXMAMAMXAAAMXMXSXSSSMSXMAAMASASXAAAMAXXAMMMMSXMXSMMXMAXXXMMMSASAXSAXAXAX
SMMSAXMMMAMAMMSAMXMSSXASAMXMXMSASAMAMMMMMSMMSSMAXMAMAMAXMMXSAAMMMSMSMSMAMAMMSSXMSAMXMMAAAAAMSXMMSAMSSMSMSSMMMAAXXAMAXAXSSMMSXXAAAMSAXMASAMMS
MAAMXXXAMAXAXMMMASMAMSMMXMAMMAMMMXSAMXAASAAXAXMXMMMMSAMSAMAMMMXMAAAAAAMASXMMAMAAAAAXAMXMMMXMMASXMAMAMXXXXAMASXSMSAMSSSMMASAMXMMXMMMXMMAMMAAM
SMMSXSSXSSXMMSAXAXMAMMXMMSMMAMXAAXXASMSMSASMMMAMXAXAXAXSAMXSAAAMSMSMAMXMAXXMASMMSAASMSXSASXMMAMASXMMSMSMSAMXMXAMXAMXMXXSAMMMXAAASXMSAMXSSMXS
XMASMASMAMASASXMAXMXMMAMAAAXSXSSSSSXAAMMSXMAXASMSSSSSSMMAMMAMMMMAAMMSMSAMXSXAXAXXAXXAAXMAMAMMSSMMXAXXAAAMXSXMSXXMAMXAXXMASAMMSMXSAAMSMAXAAAM
AMAXMAMMASMMMSASMSMAASASXMSMXAMAAXAMXMAAXASXMXMAAXAAAMXSXMAMXMAXMSMAAMASMAXMSSSMASMMSMMMAMXMAXAMMSMMMSMSMAMXXMAMSXMMMSMXAMASAAMSMMMMAMXXXMXS
SMASMMSMAMAAMSMMAAMXMAAXMAMAMXMMMMSAMXMSSMSMAMMMMMMMMMMAMXMASXXSAMMSSMXAMMXMAAAMMMSXAMSSMXAMXSAMXAAAXMAXMXSAMMAMASXAAAMMMSAMMSMAXXAXAXMSXMXS
AXMAMSMMMMSMMXMMSSMSSSMXMAMSAMXAXAXSXAMXXAMMMSAMAAAAMAMXSAMXMAXMMMAXAMSMXSAMMSMMAAXXMMMAAMSMMMAMSSSMSMXXMMAAMSASMSMMMMSAASMSAXXMXSMMSXSAASAM
MSMSMAXAXMXASXXAXAAAAAXXMASAAMSXSXMAMAAAMSMAAXASXSMXXASAMASMMSMXSMMMAMAMASASXXXSMSSSMASMMMAAMMAMMAMXXMASMSMSMMASXSASAAMMMSASXMAMMAMAMXMSSMAS
XXAASMSASXMMMXMSXMMMSMMSMMMXMMMXAMXAAXMASAMMMXXMXMASMMMXMSMXAMXXMAXMAMXMASMMXMAMAMAASAMAXXSSMMSSMSAMXMXXAAMAXMAMASAMMSMSSMXMAXAMSAMSMMAMMMMM
SMMMSXMAMAASAXMASXMXMXMASASASAXMMAXMSMSMAMSAMSMSMMXMAMASXAMMSXMASAMXSMXMASASMMAMAMMMMSSXSMAAXAAAMMAMXSSMSMSASMAMXMXMXMAXAAAMMMSXMAMAASMSMAMM
MAMAMXMAMMMMAMXMASXAAMSASMSASXSSXXSAXAAAAXSMMAAMAXXSXMAMAMXAMAXXMASAXXXMXSXMASMSXMXAAXXAMMSXMMSXMMAMAXMAXAMAXMAMAMXMXMMMSSMSMMXASMMSMMAAMASA
SAMXSXSXSXXMXMXMXSSXMXMASAMAMMXMAAMAMXMSSMSAMMSMXMAMXMMSXXMASAMMXMMASASMXMASXMASAMSMMSMSMAMAMXXAMSSMMMMMMXMXMMSSMSSMASAAMAXAASXXMMAAAMSMXXSX
SMSXAXAAMMXAAMASXMAMSMMXMXMXXSAMMMMSMMXAMXSAMSMXAAASXSAAXSMXMAMXSMMMMXAMXSMMMMSMXMAAMXXXMASXSASAMAXMXASAMXXAASAAAAAMAXMMMSMXXMMMAMMSXMXMSAMX
MAMXXMMAMAMXMSAXMXAMAMSASXSMASMXSAAMAXMAMAMAMXASXMASAMMSSXAMSAMXAAAXXMMAAMXMXSAMMMAXXAMXXAMAMXSMMSSMSSSXMAMSMMMSMSSMSSSXAMMSSMSSMMAXASAMXSAS
MAMMMAXXMXSAAMXMXSMXXSXASAAMMMSASMSSXXSAMASAMMMMSMAMMMAMAMAASASXSSMSAAXMASAMXSASMMMSAMSSMAMXMMMMAAAXSAMAMMMXASAMMMXAMAMMMMAXAAAAXMASAMASAMXS
SMSMASMXMAMXSAMXAMASMMMSMXMMSAMXSAXAMXXXMAXASAAAAMSMASXMAXXMSMXMAMXSMSSMMSASMSMMAAAXAXAAMAMXMAAMMXSMMMMASMMSAMASMSMSMAMAAMXSSMSSMMAXXSXMAMAX
AAAMSXMASMMMMXXMMSASAASAAXXAMXMMMMMMASMSMMSAMXMXXXXXMXAMASXMMASAMXASAMXAAMXAMXXXMMMXAMXSXMSXSMMSSXMAMXMAMAAMAMXMAAAASXSSSSXAXXXAMMSSMAMSSMSS
MSMSAXXAXAMXMASXAMASAMXMXMMMSMSASAMXSMASAMMAMMSMSMSMMSAMXMAAMSMXMMMMMMSMMSXSSMSMSAXMXAXMASAMXSSMMASMMAMSSMMMAAMMSMSMSXMMAXMMSXSXMAXAAMXAAAAM
XXXMASMSMSAMXAXMAXXSXMMXAMAXMAAMSASMXMMMAMSAMAAAAAAAASXMXSSMMMAMXXAAMMMMAAXAAMAAMAMSMSASXMASAMMASAMASXXXAMSXSSMXAAAXMASXSXAXAXSAMXSXMXMASMMS
XSXMASAMMMMMMMMXSAMMAMXMMSMSMAMMMAMXAXSSXMMSSSMSMSMSMXAMMMMAAXAMASMMMAMMSSMSXMMSMAMAAXASXSXMAMSAMAMMMMMSMMSAMAXXMXMXSMMAXMXMASMAMAMXSASAMAXX
AASXMMMMAXASXMSAXAXXAMAMMAAAXAMSXSMSMSAXASXMMMMAAXXXMSSMAAMMMMAMXXAASXSAAAAAMMAXMMSMSMAXMXXSXMMASAMSASAAXAMAMMMMSMSASAMMMSAMXAXAMAAASXSASAMM
XMAMAAAMXSMSAAMMMSMSSMSMXMSMSMSXAAAAXSMMASAMXASMSMMXMAMXSSSMSAMXSMSMMAMMXMMMAMAMXXAMXMMMSXASMMSXMAASAMASXMSMMXSXMASAMXMSASASAMSXSMMMSAMAMXAA
MXMSSMSMAMMMMMMAMMAXAAXMSMXAAMMMMMSMXXXAXXAMSAMSAMXAMASMMMAASXMASMAAAXSSMSSXSMSXMMMXAMAAXMAMXXSXMXMMSMAMMXAMXAMAMMMMMXMAXXAMAXMAXMMAMAMAMMSM
MXXXXAXMAMSAMASASMSMMAMAAXSSMXAAAXXXSXSSMXSMMASAMXSXSASAAXMMMMAAMASMSMAAAAAMAAAASASXSMMXMMAMXMSAMSAMXMXMXSASMSMMXSASXMSSSMSMXMMAMXMAMSSXSAXA
MMMMMXMSSMSXSAMXSAXXMXMXMMMAMSSSSSMAXASASAMXMMMMSMMAMAMMMMSAMXSXMAXAXMSMMMMXMAMMSASAXASAXXASAAMXMAASXMMSXSAMAXAMAMAMAAXAXAMAMXXXXXXAMMAAMASA
MASXMMXMXASAMMSMMMMXSAMXSXSAMMAAAMMSMXMAMMXAMAAXAAMXMSMXMXSASAMAMMMAXAXXMXSSMSXXMMMAMAMMMSASXSXMASMMAMXAMMAMAXAMMMMSMMMMMAMAMXMASMSSSMMMMXMM
SASAAXMASMMAMAAAAXSASASASASMSMMMAMAMASMSMSSSSSSSSSMXAASXMASAMXSXMXMXMAMXAAAAAXXMMMMAMXMAXMMMXMASAMXSMXSMMSMMMSAMXAMAMXAMMMSXMXSAXMAMMAXXXMAX
MASMMMAXXXSXMSSSMSAASMMMMAMAAMXXAMASXXMAAAAAXAMXAAXMSASXMAXXAMXXSXSMMMMMMASMMMXSMSMMSXMXSXSAMXXMASXMXAAXAAAAAMXMSXXASXXSAXMMMXMXSMMMSMMSSSSM
MAMMMXSXMASAMAMMMAMMMMXXMXMSMSXSXSASMASMSMAMXMXMMMXXMXXAMSSSMMAXSASAAAASXAXAASASMAXXMXSXXXMAMSMSXMAMMMMMSXXMMMAMXMSMMAMSMXSASASXSAMXAAXSAAAX
SASAMXXMMMSXMAMAXSXSAXSMMXXASAAMAMXXXAMXAXMSMMASAXMXSMMSSMAAAMSSMAMSSSMSAMSSMMASXXSXMASMMMSAMXAAXSXMASMXMSSSSSXSXMAMXMASAASMSASASXMSSSMMMMMM
MASXSMMXAMMMSMSMXMXSXSMAAXSXMMSMAMSSMSSSMMMAAMASASAAAASMAMSSMMMXMAMXMXXXAMXXAMSMMXSAMAMAXAAMXMAMXAXSSXMAAMXAXMXSASXSSXMXMMSXSAMXMMMMMAAASAMA
MMMMAAMSSMXAMXAXASAMXMMAMMSASAMXAXAAXAAXAASMSMAXAXMMXSASXMAAMXMMSASAMMXSXMXSXMXMXAXAMXSSMAXMXAXXMMXMASMMSMMXMMASMMXAXAMASXXAXXXXAAAMSSMMSASM
XSASMSXXAAMSSSSSMMAMMXXXSXSAMMXSMMSMMMSMSMSAAMSMSMSXMXAMXMSAMSXXXXSASXAMXMASXMAXMASMSMAXMAXSXMSAXXAXXAMXMASMMMASXMMSMMXAXAMSMMXMSSXMAMAMSAMM
MSASAMMMMMMAAAMAASXMASMMMAMXMMAXMAMAMAAMAAXXSMXAXAMMXMAMXXMAAXXMSXSAMMAMAMMSASASAMXAAMAMMSXSAASAMSMMAMXXSAMAAMAMASXMASMMSMAXAMSAAAMMXXAMMAMA
AMAMMMAAXAMMMMSSMMMMXSAMMAMAAMMMSASXMSSSMMMSMAMAMAMMAAASXXSMMMMSAMMAMSMMXXAMMSMSMMMSMMXSAXAMMMMMMAASMMSXMASMMMSSXMASAMXXAXXSAMAMXSMMAXSSSMMM
SMSSXMSASMSAAXXAAAXXASAMSXSSSXSAMXSAAMAAXXSAMAMMSSSSXSAMXAXMAASAMMXMXSMSMMMSXMAMXXAXAAAMMMAMAAAXMMXMAAMMSXAXAAXAXMXMAMMSMSMSAMXSXAAMMMMAAXMX
AAAXMXMAMXXMSXSSSSMMXSXMXMMXMAMASXXMMMXAMXSASMSMAAXAAXASMMMSMMSAXAXSSMAAXSASMAMSMMMSAMXAASMSSSSXXSASMMMXSMMSMSSSMXAXAMAAAAMMASMMMSMMSAMSMMMA
MMMSMSMSMSSMXMAAAAMSMMASMXSAMXSAMAXSXSXXMAXMMAAMMSMXMSMMMMMMAAMMMMSMAMMMSMAMAAXAAAAMXMSSXSAAMAXAXSAXMASAXAXAAAXAXMASXMSXSMSAAXAAAAMASAXAMAAX
XAXMMAAAXXAMSXMMMMMAAMAMAXMMXAMMMMAXAMMSMASMMSAMXXXXXMXAAMMSMMMSAXMMXXSXXMXMSSSSSMSSXMXMAMMMMAMMMMXMSMMMSMSMSMSAMXMAXAMAXXXMSSSMSMSAMXSMSMSM
SSSSSMSMSSMMSMXXXSSSSMSSSSSSXSMSAXSMMMAAMXMAAXAMXMXMASMSMXAAAMASMSMXMXAASXSAXAAAAMXAMMAMAMAMMSMMAMAMAAAMAASXMMXMASXXXXMAMASAAMXAMMMMSXSXSAAA
SAXAXAAAMXXASMMMAXAAXAMXAXAAXMASASXMAMXXSASMMMMSAMXSMXAXAMXSSMMSXAMAMMMMMAMXMMMMXSAMXSASAMMAAMMSSXXSXXMSMXMASMMMSMMMMXMXSAMSMSMXMXAMXMSAMMMX
SMSMMSMSMSMMXSAMXXMSMSMMAMMMSMMMXMASASMMMXMASXMAMXAMXMMMXSAAAXXMXMSASAAXMXMAMXSMXAXSAMMSMSSMMSAAXMMMMSXXMXSAMAAMXXAAAASMMMXXXAXMSSMXMAMAMASX
MXMXMAAXXAAXXSXMSSXAAAXXAMXAXAMSSMMSXSAAAMSAMAXASMAMAAAAAMMSMSAMSXSASMMMXAMASXMMSMXMMSAXMAMAAMMMSAXAAXXAXAMXXSMMXSSMSASXAMXMXMAAMAAXXXXSMAMA
SXAASMSMSSSMMXSXAXSMSMSSXMAMXMMAAAXXXXMMMXMXSXMASXMMSXXXSMXXASAASAMXMASMSMMAMAAAXXMXSMMSMSSMMSMASMMMSSXSMXXAXXAMAAMMMMXMASMAAXMSSMMMXSAMMSSM
SMSASXAAXXAAMASMMMSMAMXAMSMSMSMSMMMXMSMSMSMXSXXXMAXAMASMMMSMMMMMMAMSAXAASXMASMMMXMAXMAXXMAXXSAMXXAAXAMXMAMSSMSAMSSXXAMASXMASMSMAMAAAMMAMAXMX
SAMXSXMSXSSSMASAXAMMAMMMAXAAMAAXMSMMAAAAAMXAMASMMSMMSASAAAAAAXXXASMXAMXAMXXAXAAAAMXMSAMSXMSMSASXSSSSXSSMAMAAASAMXMAMAXAMAMMMAAMSSSMSXMMMXMSM
MSMAMXXAXAAAMXSAMXSXSMMXSMSMSMSMAAAAMMSMSMMXSAMAAAAXMASAMXSXMXMMMXAXMMSSMMMMSSMMMSMAXAXSAASXSAXAMAAAAAXSXMMSMSXMAMSSSMASAMAMSMSAAAAMAMSAAAXX
SXMASMSASMSMMMMXMASXAASAMMAAAAXMMMMSMMXXAXSXMASXMSMMMAMMMMXMSASAMMSMAAXAASAMAAXXAAMSMSASMMMAMAMSMMMMMMAAXMXXAMXMAAXAMXMMMMXMAMMMXMAMAMMASMMM
MAMXAAXASXMASASXMASMSMMASXMMMSMSMSAXASMSSMMXSAMAMMMAMASAAXMASASASAAXXMSMMMSMXSAMSSSMSMASXAMAMAMXAMXXXMMMXSAMAMXMMMSASAXAASMSASXSSMASAMXAMAAA
SSMMMMMSMXSAXASAMASAAAMXMASXXXAXAMASAMAAAAXAMASXMASXSSSMMSMMMASAMMSMSAMXSAMXAXMAXXXMAMAMMXSMSMXSAMSMXMSMMMMSMMAXMXMAMAMXMXAXAMXMASASASMMSXMS
AAAAMXMAAMMMMAMXMAMXMXXXSAMMMMSMMMMMAMMMMSMMSAMXSAMXMAMMMSAAMMMAMXAAXAMAMAAMXSXMMXMMXMSSMXSAMXAMAMAAAXAAMXAAASMSXAMSMSSSXXSSSMMSAMMSXMAMXXAX
SMSMSASMSMAMSAMAMAXSXMSAMXSAXAXMAAAMSMSAMAAMMXSXMASMMAMSASXMSXMMMSMSMXMASMMXSMMAMASMXMAAXAXMAMSMMMMSMSSMMMXMXAAMMMXAAXAAXMAAAAAAXXMXMAXMAMSS
XAXASAXXAMAMSASXSMXMAXAXMASXSMSSSSSSMXSASMSMMMSMMAMXXMXMMSAMXXAAASAMXMXMSMXMXAAXSASMAMSSMMSAMMXAXAXAAXAASXASXMXMAMXMSMMSXMASMMMSAASAMXSMAXAX
MAMAMAMSXSAXXAMXMXAXAMMAMXSASXAAXXMAXMSAMAXXSAMXMASMSSMAMMMMAMSMMSAXAAMSXMAAMXMXMASMSXMAAXMAXASXSMSMSMSMMAXXAAXSASAMAAXXAMAMXXXXXXMASASXSMMS
MMMMMMXMASXSMAMASXMSAXXAMXMAMMMMMXMMSMMSMAMSMMXMMASAAMMMMMAMAXXMASXMASXMAXSMMMMAMAMXXASMMMSSMMSAMXAXMAMXSXMMAMMSASMSMSMSXMSMMMSMMXSSMXSAXAXA
MAAAAXAAXMASMSMMAAAMAXSASAMAMXSASXXXMMXAMMMXXSASXSMMMSMSASMSMSMMMXMASXASMXMSAAMXMXSMXAMXSXAXAAMXMMMSMAMAMAMXAMXMAMXSAMXSAAXXAAAAMAMAMSMMMSMM
SSSSMSSSXMAMAXAXMMMMXMMASXSASXSASASMXMSXMSAAAXASMAXMASAMASAAXMAMAMXXXSXMMAAASMMAMXMASXMAMMMXMMMAMAAAMASASAMXMMSMAMXMAMASMMMSMSSSMASAMAAAAXAX
XAAAAAAMXMAXAMMXASAXSMSMSMSAXXMMMMMMAMXSAAMMSMXMXSMMAMXMAMXMMMSAMXMMMMMSXXSMAMSSMMXAAAMXMAAMMXSASMSSSMSASASXSAXXMMXMXMAMAAAXXXAMMMMXSMSMMSMM
XMSMMMSMAXSMSSXSASXSAAAMMAMAMSMSAAASMMAMSMXAMMMSMMMSSMMMXSAMAAAAXASAMXAMSMAXMMAMXXMSSMMSSMXSAASAMAAAXAMAMMAAMMSSMSMSAMXSSMSSMSAMSSMASAXAAAMA
SAMXSXXMXXXAAXASAMXMMSMSMMMAMAASXSXXMMAMAXMASAAAAMAAAAMMASASMSSMSASASMMSAXMMMMAXSAMXAAAMXMAMMMMAMMMSMSMSMAMXAMAAXASAMXMMAAMXAMSMAAMAMMSMSSSS
AMSXMASXSAMXMMAMXMASXMXAXXSXSMMMMMMMXSMSASASXMSSSMMXSAMMASMMMXXMAMSXMAXSAMXMSSXMASASXMMSAMXSXSSXMASAMXSMAXXSXMASMSMSAMXSMMMMSMXMSSMXSXXMMMXX"""
sample = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

o = 0

lines = data.split("\n")

def directional_search(x, y, xo, yo):
    for i in range(4):
        if i == 0 and lines[y][x] != "X":
            return False
        if i == 1 and lines[y][x] != "M":
            return False
        if i == 2 and lines[y][x] != "A":
            return False
        if i == 3 and lines[y][x] != "S":
            return False
        
        x += xo
        y += yo
    
    return True
        
directions = [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]

for y in range(len(lines)):
    for x in range(len(lines[y])):
        for direction in directions:
            if not (direction[0] > 0 and not x < len(lines[y]) - 3) and not (direction[1] > 0 and not y < len(lines) - 3) and not (direction[0] < 0 and not x > 2) and not (direction[1] < 0 and not y > 2):
                if directional_search(x, y, direction[0], direction[1]):
                    o += 1

print(o)