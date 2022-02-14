import dns.resolver
import sys

try:
	dom = sys.argv[1]
	
except IndexError:
	print('Syntax error: python3 dnsenum.py <domain_name>')
	quit()

rec = ['A', 'AAAA', 'MX', 'NS', 'PTR', 'TXT', 'SOA', 'CNAME']

for records in rec:
	try:
		ans = dns.resolver.resolve(dom, records)
		print(f'\n{records} Records')
		print("=" * 20)
	
		for server_result in ans:
			print(server_result.to_text())
	
	except dns.resolver.NoAnswer:
		pass
	
	except dns.resolver.NXDOMAIN:
		print(f'The domain "{dom}" does not exist! Please provide correct domain name.')
		quit()
	
	except KeyboardInterrupt:
		print('Interrupt by the user! Quitting...')
		quit()
