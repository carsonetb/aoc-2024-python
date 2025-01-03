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

def directional_search(x, y):
    if lines[y][x] != "A":
        return False
    if not ((lines[y-1][x-1] == "M" and lines[y+1][x+1] == "S") or (lines[y-1][x-1] == "S" and lines[y+1][x+1] == "M")):
        return False
    if not ((lines[y-1][x+1] == "M" and lines[y+1][x-1] == "S") or (lines[y-1][x+1] == "S" and lines[y+1][x-1] == "M")):
        return False
    return True

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if (x < len(lines[y]) - 1) and (y < len(lines) - 1) and (x > 0) and (y > 0):
            if directional_search(x, y):
                o += 1

print(o)