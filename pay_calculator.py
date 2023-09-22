hours = input("Enter hours")
rate = input("Enter rate")

hours = float(hours)
rate = float(rate)

print (" ")

pre_tax_weekly_pay = hours*rate
print (f"Pre-tax weekly pay: ${pre_tax_weekly_pay}")

pre_tax_bi_weekly_pay = pre_tax_weekly_pay*2
print (f"Pre-tax bi-weekly pay: ${pre_tax_bi_weekly_pay}")

pre_tax_monthly_pay = pre_tax_weekly_pay*4
print (f"Pre-tax monthly pay: ${pre_tax_monthly_pay}")

pre_tax_yearly_pay = pre_tax_monthly_pay*12
print (f"Pre-tax yearly pay: ${pre_tax_yearly_pay}")

print (" ")

# tax on paychecks is put at 25%
post_tax_weekly_pay = (hours*rate)*0.75
print (f"Post-tax weekly pay: ${post_tax_weekly_pay}")

post_tax_bi_weekly_pay = post_tax_weekly_pay*2
print (f"Post-tax bi-weekly pay: ${post_tax_bi_weekly_pay}")

post_tax_monthly_pay = post_tax_weekly_pay*4
print (f"Post-tax monthly pay: ${post_tax_monthly_pay}")

post_tax_yearly_pay = post_tax_monthly_pay*12
print (f"Post-tax yearly pay: ${post_tax_yearly_pay}")

print (" ")