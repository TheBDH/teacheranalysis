total_num_teachers = 0
num_emergency_cert_teachers = 0
schools = {}

for line in open('eCert.csv'):
	# print line
	cert_type = line.split('\t')[4]
	school = ""
	if len(line.split('\t')) == 11:
		school = line.split('\t')[10]
	if len(line.split('\t')) > 11:
		one = line.split('\t')[10]
		two = line.split('\t')[11]
		if len(one) > len(two):
			school = one
		else:
			school = two
	total_num_teachers += 1
	if cert_type == 'EMERGENCY':
		num_emergency_cert_teachers += 1
	if school in schools:
		schools[school]['total'] += 1
		if cert_type == 'EMERGENCY':
			schools[school]['emergency'] += 1
	else:
		schools[school] = {}
		schools[school]['total'] = 1
		if cert_type == 'EMERGENCY':
			schools[school]['emergency'] = 1
		else:
			schools[school]['emergency'] = 0

school_percentages = {}
for school in schools:
	school_percentages[school] = (float(schools[school]['emergency']) / float(schools[school]['total']) * 100.0)
highest_percentage_schools = sorted(school_percentages, key=school_percentages.get, reverse=True)[:10]

print '[INFO] TOTAL NUMBER OF CERTIFICATIONS: ' + str(total_num_teachers)
print '[INFO] NUM EMERGENCY CERTIFIED TEACHERS: ' + str(num_emergency_cert_teachers)
print '[INFO] PERCENT OF EMERGENCY CERTIFIED TEACHERS: ' + str(float(num_emergency_cert_teachers) / float(total_num_teachers) * 100.0)
print '[INFO] HIGHEST PERCENTAGE SCHOOLS: '
for school in highest_percentage_schools:
	print school + ' - ' + str(school_percentages[school])