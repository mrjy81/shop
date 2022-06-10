x = """
<link href="css/bootstrap.min.css" rel="stylesheet">
<link href="css/font-awesome.min.css" rel="stylesheet">
<link href="css/prettyPhoto.css" rel="stylesheet">
<link href="css/price-range.css" rel="stylesheet">
<link href="css/animate.css" rel="stylesheet">
<link href="css/main.css" rel="stylesheet">
<link href="css/responsive.css" rel="stylesheet">
"""

y = [i for i in x.split('\n') if i != '\n' and i != '']

for i in y:
    flag = "'"
    if '"' in x:
        flag = '"'
    a = i.split(flag)
    anti_flag = "'" if flag == '"' else "'"
    b = a[0] + anti_flag + "{% static " + flag + a[1] + flag + " %}" + anti_flag + ''.join(a[2::])
    print(b)
