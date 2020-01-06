
code = []
str1 =''
with open('12197458.tet', 'r') as f:
	for d in f:
		code.append(d)

str1 = code[0]
print(code)
print(str1)
print(len(str1))

count = 0
with open('code.tet', 'w', encoding='utf-8') as f:
	for d in str1:
		count+=1
		if count == 10 or count == 11 or count == 41 or count == 42 or count == 43 or count == 44:
			continue
		if count == 45 or count == 46 or count == 47 or count == 48 or count == 49 or count == 50:
			continue
		if count == 51 or count == 235 or count == 236 or count == 237 or count == 238 or count == 239:
			continue
		if count == 240 or count == 241 or count == 242 or count == 243 or count == 244 or count ==245:
			continue
		if count == 246 or count == 247:
			continue
		if count == 870 or count == 871 or count == 872 or count == 873 or count == 874 or count == 875:
			continue
		if count == 876 or count == 877 or count == 878 or count == 879 or count == 880 or count == 881:
			continue
		if count == 882 or count == 883 or count == 884 or count == 885 or count == 886 or count == 887:
			continue
		if count == 888 or count == 889 or count == 910 or count == 911 or count == 912 or count == 913:
			continue
		if count == 914 or count == 915 or count == 916 or count == 917 or count == 918 or count == 919 :
			continue
		if count == 1050 or count == 1051 or count == 1052 or count == 1053 or count == 1054 or count == 1055:
			continue
		if count == 1056 or count == 1057 or count == 1058 or count == 1059 or count == 1060 or count == 1061:
			continue
		if count == 1062 or count == 1063 or count == 1064 or count == 1065 or count == 1066 or count == 1067:
			continue
		if count == 1068 or count == 1069 or count == 1070 or count == 1071 or count == 1072 or count == 1074:
			continue
		if count == 1076 or count == 1077 or count == 1078 or count == 1079 or count == 1080 or count == 1081:
			continue
		if count == 1259 or count == 1260 or count == 1261 or count == 1262 or count == 1263:
			continue

		if d == ' ':
			continue
		if count == 223:
			f.write(d + '{|')
			continue
		if count == 1 or count == 9 or count == 19 or count == 24 or count == 25 or count == 34:
			f.write(d + '|')
			continue
		
		if count == 35 or count == 9 or count == 19 or count == 24 or count == 25 or count == 34:
			f.write(d + '|')
			continue
		if count == 56 or count == 92 or count == 116 or count == 128 or count == 148 or count == 158:
			f.write(d + '|')
			continue
		if count == 178 or count == 188 or count == 223 or count == 510 or count == 546 or count == 594:
			f.write(d + '|')
			continue
		if count == 642 or count == 664 or count == 684 or count == 744 or count == 766 or count == 781:
			f.write(d + '|')
			continue
		if count == 803 or count == 849 or count == 878 or count == 909 or count == 969 or count == 999:
			f.write(d + '|')
			continue
		if count == 1073 or count == 1075 or count == 1103:
			f.write(d + '|')
			continue
		if d == '{':
			f.write(d + '|')
			continue
		if count == 1082:
			f.write(d + '|' + '|')
			continue
		if d == '姐':
			f.write(d + '|')
			continue
		if count == 1113:
			f.write(d + '|' + '|' + '|')
			continue
		if count == 1258:
			f.write(d + '{')
			continue
		

		f.write(d)