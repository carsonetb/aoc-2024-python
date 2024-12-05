import copy

sample = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
data = """66|22
76|63
76|38
88|43
88|76
88|83
38|98
38|77
38|22
38|75
12|82
12|73
12|93
12|56
12|41
67|26
67|43
67|47
67|92
67|66
67|86
62|56
62|66
62|24
62|41
62|58
62|36
62|79
54|82
54|66
54|93
54|14
54|15
54|58
54|83
54|26
15|41
15|72
15|71
15|65
15|75
15|98
15|67
15|38
15|19
65|44
65|88
65|71
65|78
65|74
65|19
65|36
65|77
65|98
65|38
73|26
73|86
73|22
73|88
73|74
73|44
73|89
73|78
73|19
73|43
73|77
63|23
63|62
63|12
63|67
63|44
63|42
63|85
63|43
63|11
63|83
63|26
63|54
22|11
22|88
22|75
22|69
22|43
22|86
22|78
22|72
22|47
22|85
22|54
22|42
22|23
46|85
46|57
46|76
46|24
46|38
46|62
46|37
46|93
46|79
46|65
46|15
46|12
46|48
46|11
69|79
69|48
69|56
69|24
69|98
69|58
69|36
69|37
69|76
69|63
69|95
69|89
69|38
69|65
69|57
23|69
23|74
23|78
23|58
23|48
23|57
23|86
23|83
23|14
23|88
23|47
23|82
23|92
23|12
23|11
23|62
33|23
33|79
33|98
33|19
33|86
33|88
33|42
33|41
33|36
33|56
33|67
33|78
33|73
33|65
33|77
33|75
33|37
92|83
92|15
92|82
92|76
92|95
92|79
92|47
92|74
92|66
92|57
92|48
92|33
92|12
92|46
92|85
92|69
92|62
92|14
72|83
72|86
72|78
72|85
72|47
72|11
72|23
72|57
72|69
72|62
72|74
72|67
72|54
72|75
72|92
72|44
72|88
72|46
72|42
98|23
98|63
98|43
98|78
98|54
98|75
98|92
98|74
98|86
98|71
98|67
98|72
98|77
98|83
98|89
98|42
98|88
98|11
98|12
98|46
77|26
77|54
77|75
77|42
77|14
77|47
77|62
77|12
77|74
77|69
77|67
77|86
77|11
77|22
77|46
77|92
77|85
77|78
77|44
77|88
77|23
56|72
56|92
56|74
56|26
56|67
56|78
56|75
56|44
56|63
56|88
56|46
56|89
56|83
56|42
56|98
56|14
56|71
56|19
56|23
56|86
56|43
56|54
14|82
14|66
14|38
14|95
14|15
14|41
14|69
14|85
14|47
14|12
14|62
14|37
14|24
14|79
14|11
14|57
14|36
14|48
14|76
14|33
14|73
14|58
14|65
86|12
86|58
86|62
86|95
86|76
86|14
86|15
86|92
86|85
86|54
86|47
86|66
86|82
86|83
86|46
86|26
86|69
86|43
86|74
86|24
86|57
86|78
86|11
86|48
41|86
41|72
41|36
41|89
41|78
41|98
41|43
41|42
41|19
41|23
41|56
41|92
41|63
41|73
41|67
41|37
41|88
41|44
41|75
41|65
41|22
41|71
41|38
41|77
11|93
11|57
11|41
11|58
11|95
11|69
11|15
11|38
11|73
11|37
11|85
11|82
11|56
11|65
11|76
11|24
11|33
11|79
11|62
11|48
11|36
11|47
11|19
11|66
82|63
82|71
82|19
82|65
82|41
82|44
82|73
82|95
82|79
82|38
82|37
82|98
82|93
82|56
82|36
82|77
82|33
82|75
82|24
82|15
82|72
82|48
82|89
82|22
79|22
79|88
79|86
79|38
79|63
79|42
79|72
79|67
79|23
79|56
79|98
79|77
79|43
79|71
79|41
79|36
79|44
79|73
79|37
79|75
79|89
79|78
79|19
79|65
58|89
58|65
58|98
58|63
58|93
58|95
58|24
58|33
58|15
58|77
58|71
58|48
58|82
58|41
58|19
58|38
58|66
58|79
58|73
58|57
58|56
58|36
58|76
58|37
85|58
85|15
85|36
85|38
85|41
85|76
85|57
85|95
85|82
85|33
85|71
85|66
85|93
85|24
85|56
85|37
85|79
85|48
85|19
85|73
85|69
85|98
85|47
85|65
19|98
19|86
19|78
19|83
19|22
19|14
19|63
19|72
19|42
19|23
19|74
19|67
19|44
19|26
19|54
19|71
19|77
19|89
19|12
19|43
19|92
19|75
19|88
19|46
74|66
74|24
74|14
74|93
74|46
74|83
74|48
74|47
74|15
74|82
74|41
74|58
74|62
74|54
74|57
74|26
74|85
74|11
74|33
74|95
74|12
74|79
74|69
74|76
71|63
71|11
71|22
71|67
71|46
71|14
71|74
71|89
71|86
71|72
71|12
71|77
71|42
71|92
71|78
71|23
71|62
71|88
71|83
71|26
71|75
71|44
71|43
71|54
42|78
42|85
42|14
42|48
42|26
42|74
42|46
42|69
42|47
42|54
42|57
42|62
42|66
42|76
42|43
42|92
42|86
42|15
42|12
42|58
42|11
42|95
42|82
42|83
83|57
83|36
83|46
83|24
83|79
83|82
83|93
83|47
83|48
83|95
83|26
83|14
83|58
83|12
83|69
83|33
83|85
83|66
83|15
83|41
83|62
83|65
83|76
83|11
57|56
57|95
57|65
57|89
57|33
57|38
57|98
57|93
57|24
57|48
57|82
57|63
57|19
57|79
57|37
57|66
57|73
57|22
57|71
57|77
57|41
57|36
57|76
57|15
24|93
24|63
24|23
24|88
24|75
24|98
24|56
24|73
24|79
24|36
24|77
24|42
24|72
24|44
24|65
24|33
24|41
24|37
24|19
24|71
24|38
24|22
24|89
24|67
48|63
48|93
48|19
48|73
48|67
48|36
48|22
48|38
48|33
48|56
48|44
48|24
48|77
48|72
48|37
48|79
48|98
48|71
48|95
48|15
48|41
48|75
48|89
48|65
95|33
95|19
95|24
95|44
95|72
95|79
95|22
95|65
95|37
95|67
95|63
95|73
95|89
95|23
95|38
95|75
95|41
95|88
95|71
95|98
95|56
95|77
95|93
95|36
78|76
78|69
78|62
78|15
78|43
78|47
78|92
78|24
78|46
78|48
78|85
78|95
78|93
78|54
78|11
78|66
78|12
78|83
78|58
78|82
78|74
78|14
78|26
78|57
44|88
44|26
44|78
44|47
44|86
44|67
44|92
44|57
44|12
44|11
44|85
44|76
44|14
44|42
44|75
44|69
44|23
44|46
44|43
44|62
44|54
44|58
44|83
44|74
43|12
43|82
43|92
43|14
43|85
43|74
43|76
43|62
43|33
43|95
43|11
43|66
43|46
43|15
43|69
43|47
43|24
43|26
43|57
43|83
43|48
43|58
43|93
43|54
47|65
47|38
47|24
47|73
47|58
47|98
47|56
47|89
47|48
47|93
47|36
47|76
47|41
47|71
47|95
47|66
47|33
47|57
47|79
47|15
47|37
47|82
47|69
47|19
37|38
37|23
37|74
37|98
37|73
37|88
37|89
37|75
37|77
37|44
37|71
37|86
37|43
37|42
37|22
37|19
37|83
37|72
37|54
37|78
37|56
37|63
37|67
37|92
26|66
26|95
26|65
26|82
26|85
26|48
26|15
26|37
26|69
26|47
26|57
26|58
26|62
26|46
26|24
26|79
26|14
26|33
26|76
26|41
26|12
26|36
26|93
26|11
93|56
93|22
93|44
93|65
93|71
93|88
93|38
93|75
93|36
93|72
93|86
93|63
93|79
93|67
93|23
93|73
93|41
93|19
93|37
93|33
93|77
93|42
93|98
93|89
75|86
75|11
75|46
75|14
75|76
75|54
75|26
75|67
75|85
75|74
75|69
75|42
75|66
75|92
75|47
75|83
75|23
75|88
75|78
75|57
75|43
75|62
75|12
75|58
89|92
89|77
89|63
89|86
89|78
89|12
89|67
89|46
89|85
89|74
89|26
89|44
89|54
89|72
89|22
89|43
89|83
89|14
89|88
89|11
89|75
89|62
89|42
89|23
36|43
36|23
36|22
36|72
36|71
36|54
36|73
36|74
36|56
36|78
36|63
36|89
36|38
36|37
36|19
36|77
36|88
36|42
36|98
36|67
36|92
36|44
36|86
36|75
66|44
66|65
66|33
66|77
66|95
66|89
66|63
66|71
66|56
66|82
66|98
66|36
66|79
66|15
66|19
66|73
66|72
66|48
66|37
66|41
66|24
66|38
66|93
76|36
76|48
76|73
76|56
76|24
76|93
76|33
76|77
76|19
76|95
76|66
76|41
76|98
76|71
76|22
76|37
76|65
76|15
76|82
76|79
76|72
76|89
88|47
88|69
88|26
88|78
88|82
88|62
88|14
88|86
88|66
88|74
88|48
88|11
88|85
88|15
88|58
88|12
88|92
88|57
88|46
88|54
88|42
38|23
38|92
38|44
38|43
38|54
38|63
38|26
38|19
38|73
38|42
38|71
38|78
38|88
38|56
38|74
38|86
38|72
38|89
38|83
38|67
12|33
12|76
12|62
12|66
12|85
12|95
12|69
12|11
12|38
12|57
12|79
12|58
12|15
12|24
12|48
12|65
12|37
12|36
12|47
67|23
67|85
67|12
67|82
67|88
67|58
67|78
67|57
67|42
67|46
67|14
67|11
67|54
67|69
67|62
67|76
67|83
67|74
62|33
62|76
62|95
62|19
62|15
62|85
62|82
62|38
62|93
62|37
62|73
62|69
62|65
62|57
62|48
62|98
62|47
54|76
54|79
54|48
54|12
54|47
54|33
54|24
54|62
54|46
54|57
54|65
54|11
54|95
54|69
54|85
54|41
15|44
15|73
15|63
15|89
15|93
15|22
15|36
15|24
15|56
15|37
15|33
15|77
15|95
15|79
15|23
65|92
65|72
65|43
65|63
65|86
65|75
65|73
65|89
65|22
65|42
65|67
65|23
65|56
65|37
73|98
73|67
73|72
73|83
73|42
73|56
73|75
73|54
73|92
73|71
73|63
73|23
73|46
63|14
63|77
63|22
63|74
63|47
63|78
63|46
63|72
63|92
63|88
63|86
63|75
22|26
22|14
22|74
22|92
22|46
22|58
22|62
22|83
22|44
22|67
22|12
46|36
46|47
46|58
46|14
46|41
46|66
46|69
46|82
46|95
46|33
69|66
69|93
69|15
69|33
69|73
69|82
69|19
69|71
69|41
23|76
23|46
23|42
23|85
23|26
23|66
23|54
23|43
33|63
33|44
33|89
33|71
33|72
33|22
33|38
92|11
92|54
92|24
92|58
92|26
92|93
72|14
72|12
72|26
72|43
72|58
98|44
98|26
98|14
98|22
77|43
77|83
77|72
56|77
56|22
14|93

11,62,85,47,69,58,57,76,66,82,48,15,95,24,93,33,79,41,65,36,37,38,56
42,86,69,46,92,76,43,62,11,54,57,74,47,85,12,66,26,83,48,14,78
77,22,75,67,23,88,78,92,83,26,14,11,62
19,44,98,65,56,41,36,24,33,22,38,48,77,75,73,15,63
54,83,11,62,47,69,66,82,48,93,41
95,33,79,36,38,98,89,63,77,72,23
85,47,76,82,48,79,65,36,38,73,19
33,24,65,41,98,85,37,79,19,15,38,48,76,82,56,95,57
46,14,12,11,62,85,47,69,58,57,76,82,15,24,93,33,79,41,65,36,37
33,79,41,73,98,71,22,44,75,67,23,88,86
58,57,76,66,82,48,15,95,24,41,65,37,38,73,56,98,71,89,63
41,62,69,12,38,14,76
23,38,73,72,89,71,88,37,42,41,22,86,44,63,43,75,19,77,56
15,48,62,58,47,66,69,78,11,82,83,76,46,95,26
95,24,93,33,79,41,65,36,38,56,19,98,71,89,77,22,72,44,75,67,23
71,73,57,38,66,93,24,77,19
73,43,89,75,98,63,72,36,42,41,38,67,19,78,23
95,15,24,65,58,36,85,46,14,33,82
11,83,92,66,15,47,86,46,54,48,26,78,57,74,82,85,62,69,14
75,78,54,83,67,74,88,72,62,22,86,85,46,26,43,42,44,77,14,47,12
67,23,88,42,86,78,43,92,74,54,83,26,46,14,12,62,85,69,57,76,66
75,19,63,86,83,92,88,44,77,72,14
58,76,38,57,98,82,73,48,41,95,85,93,36,56,15,79,66,65,47
98,89,44,22,23,79,36,77,41,71,38,56,65,37,75,33,88,67,72
75,88,56,41,72,89,24
48,15,95,24,33,79,41,36,37,38,73,71,77,22,72,44,75
89,63,77,22,72,44,75,67,23,88,42,86,43,92,74,83,46,14,12,11,62
82,48,93,79,56
65,36,38,73,56,19,71,89,63,44,88,42,92
67,38,65,19,63,77,71,89,42,22,73,44,72,56,37,41,36,98,33,88,23
63,22,75,88,42,86,78,26,46,14,11
76,66,82,48,95,24,79,41,37,38,73,56,19,98,71,89,63,77,22
41,71,44,73,19,79,98,24,37,82,72,22,89,33,65
54,56,23,77,75,44,92,73,26,78,67,19,74
71,12,11,63,26,46,42,88,83,78,44
57,15,73,24,12,48,85
44,75,86,92,46,12,69,58,57
79,23,73,38,42,72,19,86,41,36,77,33,63,67,37
65,98,73,43,86,72,22,56,88,36,63,41,42,71,37
72,44,88,42,54,26,46,14,12,62,47,69,58
24,93,79,41,38,73,56,98,63,77,22,72,75,67,88
44,65,67,36,92,78,22
75,23,83,12,62,57,76
24,79,41,65,73,56,71,77,72
15,82,71,48,66,79,63,72,38
76,95,33,79,41,73,89,63,22
85,76,15,79,65
79,41,65,36,37,38,73,56,19,98,89,63,77,22,72,75,67,23,88,86,78
85,47,69,58,57,76,66,82,48,15,95,24,93,79,41,37,38,73,56,19,98
63,77,72,44,75,67,23,88,42,86,78,43,92,74,54,83,26,46,14,12,11,62,85
92,47,58,66,14,69,15,33,24
26,48,93,69,24
22,75,26,19,71,98,74,23,63,43,44,88,89,92,78,56,72,54,67,83,73
78,43,46,85,69,76,24
22,23,56,83,44,38,92,77,43,98,54,74,89,72,63,19,42
67,23,88,43,74,54,14,47,69,57,66
66,82,88,74,47,83,43,62,26,92,78,86,42,54,23,14,85,58,12,11,76
89,63,77,22,72,44,75,23,88,42,86,78,43,92,74,54,83,26,46,14,12,11,62
36,73,71,89,22
48,82,62,76,43,54,88
33,15,58,57,92,74,93
19,89,69,37,57,58,36,73,98
15,79,41,73,19,98,71,89,77,22,44,75,67
58,15,24,65,36
93,33,79,41,37,38,19,98,89,63,77,22,72,44,67,88,42
41,65,36,73,98,89,63,77,72,44,75,67,42,78,43
78,92,83,12,11,48,95
69,44,75,26,47,14,83,67,11,57,46
71,48,56,36,19,72,15,33,79,38,75
12,79,66,58,95,93,82,15,73,48,85,41,24,47,33,69,62
72,36,71,89,33,38,44,79,37,65,93,67,63,77,98,19,41,24,75,73,15,56,95
33,38,15,66,56,19,79,41,62,37,82,57,58
86,78,43,92,74,54,83,26,46,14,11,62,85,47,69,58,57,76,66,82,48,15,95
72,38,71,89,77,75,36,19,67,63,88,73,37,43,22,98,41,65,23,44,42
38,93,14,58,48,15,57,65,62,69,76,82,47,79,36
79,65,36,73,56,19,63,22,75
89,36,72,38,23,73,71,63,37,98,65,22,33,19,79,77,44,67,93,24,56,41,88
54,23,44,74,72,56,67,83,75,77,22,92,38
86,44,85,83,22,67,63,77,92,72,78,74,14,54,88
83,26,46,12,62,85,47,69,58,57,76,66,82,48,15,95,93,33,79,41,65
69,58,57,76,48,24,33,79,65,19,89
79,38,82,11,69,12,36,66,15,41,95,33,76,85,24,58,57
72,67,71,19,22,41,77,63,37,42,33,65,56,44,75,89,88
57,76,66,48,15,95,24,93,33,79,41,65,36,37,38,73,56,19,98,71,89,63,77
67,83,92,19,23,71,44,63,56,74,77,54,22,46,89,75,86,98,78
93,33,79,41,65,36,37,73,56,19,98,71,89,63,77,22,72,44,75,67,23,88,42
19,75,44,77,83,72,22,73,54,26,78,89,63,56,86
62,85,66,48,15,36,38,56,19
71,75,67,42,78,92,14
48,12,47,24,65,41,76,57,95,82,85,62,79,58,15,66,73
65,37,89,23,22,78,42,86,77,67,79,88,72
37,76,47,33,62,57,19,79,95
19,63,75,23,78,43,26,46,14
78,22,65,38,19,98,89
65,66,82,98,48,15,95,73,24,69,37,58,76,93,57,47,79,41,85
12,43,75,42,54,58,92,47,11,86,83
38,73,98,71,63,77,22,72,44,67,88,42,78,92,74
71,89,63,75,88,42,78,92,12
33,82,38,72,89,22,98,66,19,65,48,41,77,73,15
71,57,38,73,47,58,48,41,37,79,24,15,33
98,71,63,77,22,75,88,86,43,92,74,54,83,26,46,14,12
43,92,54,83,26,46,12,11,62,85,47,69,58,57,76,66,82,48,95,24,93
23,56,22,86,88,19,72,75,71,65,77
67,23,88,42,86,78,43,92,74,54,83,26,46,14,11,62,85,47,69,58,57,76,66
47,69,57,15,36,19,98
89,22,44,75,23,88,86,78,43,92,54,26,46,14,12,11,62
22,37,19,36,74,42,88,23,77,72,56,98,38,73,78
58,57,76,82,15,24,41,65,36,37,73,19,71
42,86,43,92,54,83,46,14,11,62,58,57,76,66,82
46,75,63,86,56,72,71
77,71,46,22,44,72,67,14,78,12,89
75,63,12,88,62,77,72,86,92,22,23,89,78,11,42,54,83,14,46
73,33,37,67,72,42,36,44,23,98,19,88,41,89,79,77,65,75,56,93,38
78,63,43,75,42,92,71,77,72,12,44
12,48,85,36,38,11,37,76,95,65,15,24,41,14,62,33,82,47,66
58,85,57,65,11,24,37,48,33,12,82,76,79
44,56,36,82,48,95,63,33,98,37,65
85,47,58,57,82,48,79,65,73,19,98
46,14,11,62,85,69,58,66,82,95,24,93,41,36,37
26,43,71,83,67,23,22,86,78,74,75,73,98,88,19,77,56
58,57,76,66,82,48,15,95,24,93,33,79,41,65,36,37,38,56,19,98,71,89,63
15,95,79,41,36,37,38,73,19,98,71,77,72,75,67
43,98,54,86,72,92,14,63,46,23,26,74,77,89,19
85,65,93,76,79,41,58,47,69,11,24,33,95,15,82,83,14,48,26,57,46,66,62
77,73,63,67,86,22,56,41,89,19,65,43,37
76,24,93,38,95,66,82,65,69,56,89,37,79,57,36
67,88,42,78,43,92,74,54,83,26,46,14,12,11,62,85,47,69,57,76,66
92,66,82,93,85,12,58,11,48,43,47,74,24
69,95,11,12,47,54,86,82,43
15,24,77,72,44
89,71,88,73,75,86,41,19,37,63,65,38,33,56,67,42,44
36,37,38,19,71,89,63,77,72,44,67,23,42,92,74
67,88,86,43,92,74,54,83,46,14,12,11,62,85,47,69,57,76,66
85,76,83,95,14,74,86,46,57,62,92,78,12,47,58
66,82,15,24,93,33,79,41,65,36,37,38,73,56,89
22,72,44,75,67,23,88,42,86,78,43,92,74,54,83,26,46,14,12,11,62,85,69
65,75,23,93,33,41,37,77,79,88,72,19,56,38,44,67,89
69,58,57,76,66,82,15,95,24,93,33,79,41,65,36,37,73,56,98,71,89
43,92,74,83,26,46,14,12,11,62,85,47,69,58,57,76,66,82,48,15,95,24,93
36,65,37,38,57,48,85,41,19,56,79,58,66,24,15,33,82,62,73
98,63,77,22,67,88,86,92,74,83,26,14,12
26,66,48,83,93,12,62,79,14,57,82,33,69,24,74
33,22,23,79,63,95,75,71,36,93,72,24,56,67,98
57,82,48,15,93,33,79,41,36,37,56,71,77
41,46,93,57,58,36,15,62,69,65,37,11,33
69,58,76,66,82,48,95,24,33,79,37,38,19,98,71
42,12,78,83,43,74,86,58,76,69,46,48,26,82,11,14,85,92,47
24,33,79,41,65,36,73,56,98,89,77,22,72,44,88
19,22,73,65,33,63,36,48,15,93,71,66,89,77,72,37,82
36,11,62,41,93,82,66,79,47,24,15,57,95,65,56,38,58
95,14,93,46,74,48,58,62,11,83,33,66,92
83,38,88,71,22,89,78,86,56
66,82,48,95,24,33,41,65,36,37,38,19,98,71,77,22,72
85,33,93,95,14,62,47,57,48,76,58,69,12,82,38,24,11
19,98,71,89,63,77,22,44,75,23,88,42,78,92,74,54,83,26,14
14,26,92,44,86,42,78,74,89,22,75,62,67,11,77,12,43
85,47,69,58,57,76,66,82,48,15,95,24,93,33,79,41,65,36,37,38,73,56,19
43,22,73,88,78,38,72,86,71,67,98,63,92,77,74,23,19,36,56
42,86,78,43,74,54,83,26,46,14,12,11,62,85,47,69,58,57,76,48,15
62,33,85,82,66,12,95,24,26,92,83,58,76,69,93,57,46
67,78,74,46,11,69,76
66,79,24,65,12,83,57,62,58,46,69,93,76,33,14
19,83,77,54,42,38,98,89,75,86,92
93,62,37,11,65,41,38,12,15,69,47,58,66,48,24,33,76,14,36,85,79
57,93,79,56,11,48,38
77,22,75,67,23,88,78,43,74,83,26,14,47
24,79,41,38,73,56,19,71,89,77,72,44,67,23,88
57,12,85,62,92,76,26,47,69
65,37,38,56,19,98,71,63,72,44,67,23,42
63,33,37,19,77,98,79,48,75
23,88,42,86,78,43,92,74,54,83,26,46,14,11,62,85,47,69,57,66,82
56,73,72,83,43,38,71,77,44,92,75,67,88
79,75,41,56,36,98,93,44,63,19,24,38,77,65,33,72,22,95,71,73,67,23,37
14,42,85,47,43
89,43,74,63,78,92,42,77,88,86,22,83,72,67,56,73,26,23,98
56,19,98,71,72,44,75,23,78,43,92,74,54,26,46
83,85,11,12,54,82,93,62,79,57,76,46,24,69,14,74,66,48,15
54,22,83,77,67,75,23,26,14,44,11,78,63,72,43,12,92,46,86,89,71
73,19,98,71,89,63,77,22,72,44,75,67,23,88,42,86,78,43,92,74,54,83,26
86,83,67,88,73,38,23
54,62,58,78,74,11,48,14,66,76,57,88,69,46,12,43,47,26,42,83,86,82,85
12,62,58,82,95,41,73
83,14,12,11,62,76,66,48,15,95,93,79,65
69,15,33,79,65,36,37,73,89
77,19,24,89,48,71,33,98,37,79,95,65,22,93,82,41,76
19,93,38,56,44,89,37,79,48,36,22,63,82,98,41,33,73,15,77
47,86,69,12,72,26,62,85,23,11,42,22,54,67,43,44,75,46,83
62,47,65,58,76,24,36,33,57,41,12,14,82
43,42,86,88,44,89,72,67,19,74,23,54,92,63,71,78,14,77,75,22,26
72,75,42,78,43,83,46,69,58
23,88,62,47,69,66,82
22,98,75,38,72,37,23,19,92"""

ordering = data.split("\n\n")[0]
updates = data.split("\n\n")[1]

rules = {}
o = 0

for rule in ordering.split("\n"):
    split = rule.split("|")
    if rules.get(split[0]):
        rules[split[0]].append(split[1])
    else:
        rules[split[0]] = [split[1]]

for update in updates.split("\n"):
    split = update.split(",")
    checked = []
    failed = False
    for i in range(len(split) - 1, -1, -1):
        if not rules.get(split[i]):
            checked.append(split[i])
            continue

        for after in rules[split[i]]:
            if after in checked or not after in update or after == split[i]:
                continue

            failed = True
            break
        
        if failed:
            break

        checked.append(split[i])
    
    if failed:
        is_sorted = False
        while not is_sorted:
            reached_end = True
            ind = -1
            for num in split:
                ind += 1
                for after in split[ind+1:]:
                    if not rules.get(after):
                        print("CONTINUE")
                        continue
                    if num in rules[after]:
                        a, b = split.index(num), split.index(after)
                        split[b], split[a] = split[a], split[b]
                        reached_end = False
                        print("FAIL:", num, after, rules[after], split)
                        break

                    print("SUCCESS:", num, after, rules[after], split)
                print(is_sorted, reached_end)
            
            print("HI")
            if reached_end:
                print("HI")
                is_sorted = True

        o += int(split[(len(split) - 1) // 2])


print(o)