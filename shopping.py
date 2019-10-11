import random
from PIL import Image     
import time             #  import PIL libraries so that it enables to pop images using terminals

z=1
print("WELCOME  TO  BALLAYA  ONLINE  SHOPPING   CLI  APPLICATION.")
time.sleep(0.2)
print("Enter your account email ID")           # email 
while(z!=0):
	user=input()      
	length=len(user)               #  length of input
	for i in range(length):
		if(user[i]=="@" or user[i]=="."):
			z=z+1
	if(z==3):	
		print("Enter your password")
		print("enter everything you have")
		print("I am very happy boy")
		
		user=input()
		print("Please wait .....")
		time.sleep(2)
		print("Successfully login")
		time.sleep(0.5)
		z=0
	else:
		print("Please enter valid email address")            # if user gives a wrong input then it ask again
		z=1
shopping_list=[]        #   all the items will be added to this list
shopping_list_cost=[]             # all the item costs will be added to this list
z=1                #   to make shopping list shown multiple times
cnt=0         #  cnt variable counts the number of items
user=""           # all the user inputs are stored in user variable
print("Press 'ENTER' to continue")
x=input()
print("******************************************************************************************************************************************")
print("******************************************************************************************************************************************")
while(z!=0):     #main program begins  here.
	print("Please choose category")
	print("1 Mens wear")
	time.sleep(0.2)
	print("2 Womens wear")
	time.sleep(0.2)	
	print("3 Mobiles and laptops")
	time.sleep(0.2)
	print("4 Books")
	time.sleep(0.2)
	print("5 BALLAYA echo and TV stick")
	time.sleep(0.2)
	print("6 Groceries")
	time.sleep(0.2)
	print("**************Press '0' to exit **************")
	print("******************************************************************************************************************************************")
	print("******************************************************************************************************************************************")
	user=input()
	if(user=="1"):   # mens wear -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		gst=0            # this variable is a basic value that is added to different brands , if you examine carefully different sizes have different gst values and different prices.
		print("1 T-shirt ")
		print("2 Formal shirts")
		print("3 Jeans")
		print("4 Trousers")
		print("******************************************************************************************************************************************")
		print("******************************************************************************************************************************************")
		user=input()
		if(user=="1"):   # t shirt
			f=0      #  it is used to permit into the brand options  
			shopping_list.append("t-shirt")
			print("select the size( S,L,M,XL,XXL )")
			print("******************************************************************************************************************************************")
			print("******************************************************************************************************************************************")
			user=input().lower()                       #   initial choosing size will changes the gst 
			if(user=="s"):
				shopping_list[cnt]=shopping_list[cnt]+" S"
				f=1           
				gst=50              #    choosing size will changes the gst  value
			elif(user=="l"):
				shopping_list[cnt]=shopping_list[cnt]+" L"	
				f=1
				gst=100
			elif(user=="m"):
				shopping_list[cnt]=shopping_list[cnt]+" M"
				f=1
				gst=150
			elif(user=="xl"):
				shopping_list[cnt]=shopping_list[cnt]+" XL"	
				f=1
				gst=200
			elif(user=="xxl"):
				shopping_list[cnt]=shopping_list[cnt]+" XXL"	
				f=1
				gst=250
			else:
				shopping_list.pop(cnt)         #  In case user presses a wrong key, then the item is popped out from the list
			if(f==1):
				print("Choose the brand")                                   #       choosing brand will make respective changes in prices
				print("1 US polo    RS."+str(gst+450))
				print("2 Baffalo      RS."+str(gst+500))
				print("3 Ballaya     RS."+str(gst+600))
				print("4 Fasaaak    RS."+str(gst+550))
				user=input()	
				if(user=="1"):
					shopping_list[cnt]=shopping_list[cnt]+" US polo"	   #    finally adding items  to cart
					shopping_list_cost.append(gst+450)                         #    finally adding  items price to list
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="2"):
					shopping_list[cnt]=shopping_list[cnt]+" Baffalo"	
					shopping_list_cost.append(gst+500)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="3"):
					shopping_list[cnt]=shopping_list[cnt]+" Ballaya"                                    #    most famous brands .TRY   IT
					shopping_list_cost.append(gst+600)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="4"):
					shopping_list[cnt]=shopping_list[cnt]+" Fasaaak"                                        #       most famous brand .TRY  IT
					shopping_list_cost.append(gst+550)
					cnt=cnt+1
					print("Successfully added to cart.")
				else:
					shopping_list.pop(cnt)
		elif(user=="2"):   # formal shirt
			f=0
			shopping_list.append("formal_shirt")
			print("select the size( S,L,M,XL,XXL )")
			print("******************************************************************************************************************************************")
			print("******************************************************************************************************************************************")
			user=input()
			if(user=="s"):
				shopping_list[cnt]=shopping_list[cnt]+" S"
				f=1
				gst=50
			elif(user=="l"):
				shopping_list[cnt]=shopping_list[cnt]+" L"	
				f=1
				gst=100
			elif(user=="m"):
				shopping_list[cnt]=shopping_list[cnt]+" M"
				f=1
				gst=150
			elif(user=="xl"):
				shopping_list[cnt]=shopping_list[cnt]+" XL"	
				f=1
				gst=200
			elif(user=="xxl"):
				shopping_list[cnt]=shopping_list[cnt]+" XXL"	
				f=1
				gst=250
			else:
				shopping_list.pop(cnt)
			if(f==1):
				print("Choose the brand")
				print("1 US polo    RS."+str(gst+450))
				print("2 Baffalo      RS."+str(gst+500))
				print("3 Ballaya     RS."+str(gst+600))
				print("4 Fasaaak   RS."+str(gst+550))
				user=input()
				if(user=="1"):
					shopping_list[cnt]=shopping_list[cnt]+" US polo"	
					shopping_list_cost.append(gst+450)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="2"):
					shopping_list[cnt]=shopping_list[cnt]+" Baffalo"	
					shopping_list_cost.append(gst+500)
					print("Successfully added to cart.")
					cnt=cnt+1
				elif(user=="3"):
					shopping_list[cnt]=shopping_list[cnt]+" Ballaya"
					shopping_list_cost.append(gst+600)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="4"):
					shopping_list[cnt]=shopping_list[cnt]+" Fasaaak"
					shopping_list_cost.append(gst+550)
					cnt=cnt+1
					print("Successfully added to cart.")
				else:
					shopping_list.pop(cnt)
		elif(user=="3"):  # jeans
			shopping_list.append("jeans")
			print("Choose the brand")
			print("1 US polo    RS.750")
			print("2 Baffalo      RS.700")
			print("3 Ballaya     RS.1200")
			print("4 Lee            RS.600")
			print("5 Urbano      RS.650")
			user=input()	
			if(user=="1"):
				shopping_list[cnt]=shopping_list[cnt]+" US polo"	
				shopping_list_cost.append(750)
				print("Successfully added to cart.")
				cnt=cnt+1
			elif(user=="2"):
				shopping_list[cnt]=shopping_list[cnt]+" Baffalo"	
				shopping_list_cost.append(700)
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="3"):
				shopping_list[cnt]=shopping_list[cnt]+" Ballaya"
				shopping_list_cost.append(1200)
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="4"):
				shopping_list[cnt]=shopping_list[cnt]+" Lee"
				shopping_list_cost.append(600)
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="5"):
				shopping_list[cnt]=shopping_list[cnt]+" Urbano"
				shopping_list_cost.append(650)
				cnt=cnt+1
				print("Successfully added to cart.")
		elif(user=="4"):   # trousers
			shopping_list.append("trousers")
			print("Choose the brand")
			print("1 US polo    RS.650")
			print("2 Baffalo      RS.600")
			print("3 Ballaya     RS.1100")
			print("4 Lee            RS.500")
			print("5 Urbano      RS.550")
			user=input()	
			if(user=="1"):
				shopping_list[cnt]=shopping_list[cnt]+" US polo"	
				shopping_list_cost.append(650)
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="2"):
				shopping_list[cnt]=shopping_list[cnt]+" Baffalo"	
				shopping_list_cost.append(600)
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="3"):
				shopping_list[cnt]=shopping_list[cnt]+" Ballaya"
				shopping_list_cost.append(1200)
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="4"):
				shopping_list[cnt]=shopping_list[cnt]+" Lee"
				shopping_list_cost.append(500)
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="5"):
				shopping_list[cnt]=shopping_list[cnt]+" Urbano"
				shopping_list_cost.append(550)
				cnt=cnt+1
				print("Successfully added to cart.")
		user=""
		print("If you want to continue shopping  press 'Enter' .\n To exit press '0'   "  )        # asking the user wheather the user wants to continue or not 
		e=input()
		if(e=="0"):
			z=0
		else:
			z=1
		for i in range(10):                      #   small loop that simple created multiple enter to make the application look beautiful
			for j in range(10):
				print()
		print("******************************************************************************************************************************************")
		print("******************************************************************************************************************************************")

	elif(user=="2"):    # womens wear --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		gst=0             # gst is also different for different clothing
		print("1 Leggings")
		print("2 Jeans")
		print("3 Sarees")
		print("4 Tops")
		print("******************************************************************************************************************************************")
		print("******************************************************************************************************************************************")
		user=input()
		if(user=="1"):   # leggings
			f=0
			shopping_list.append(" Leggings")
			print("select the size( S,L,M,XL,XXL )")
			print("******************************************************************************************************************************************")
			print("******************************************************************************************************************************************")
			user=input().lower()
			if(user=="s"):
				shopping_list[cnt]=shopping_list[cnt]+" S"
				f=1
				gst=50
			elif(user=="l"):
				shopping_list[cnt]=shopping_list[cnt]+" L"	
				f=1
				gst=100
			elif(user=="m"):
				shopping_list[cnt]=shopping_list[cnt]+" M"
				f=1
				gst=150
			elif(user=="xl"):
				shopping_list[cnt]=shopping_list[cnt]+" XL"	
				f=1
				gst=200
			elif(user=="xxl"):
				shopping_list[cnt]=shopping_list[cnt]+" XXL"	
				f=1
				gst=250
			else:
				shopping_list.pop(cnt)
			if(f==1):
				print("Choose the brand")
				print("1 Prisma    RS."+str(gst+250))
				print("2 Lyra         RS."+str(gst+300))
				print("3 Ballaya     RS."+str(gst+400))
				print("4 Fasaaak  RS."+str(gst+550))
				user=input()	
				if(user=="1"):
					shopping_list[cnt]=shopping_list[cnt]+" Prisma"	
					shopping_list_cost.append(gst+250)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="2"):
					shopping_list[cnt]=shopping_list[cnt]+" Lyra"	
					shopping_list_cost.append(gst+300)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="3"):
					shopping_list[cnt]=shopping_list[cnt]+" Ballaya"
					shopping_list_cost.append(gst+400)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="4"):
					shopping_list[cnt]=shopping_list[cnt]+" Fasaaak"
					shopping_list_cost.append(gst+550)
					cnt=cnt+1
					print("Successfully added to cart.")
				else:
					shopping_list.pop(cnt)
			
		elif(user=="2"):   # jeans
			shopping_list.append(" Jeans")
			print("Choose the brand")
			print("1 Urban Navy   RS.450")
			print("2 Trinity    RS.500")
			print("3 Ballaya     RS.600")
			user=input()
			if(user=="1"):
				shopping_list[cnt]=shopping_list[cnt]+" Urban Navy"	
				shopping_list_cost.append(450)
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="2"):
				shopping_list[cnt]=shopping_list[cnt]+" Trinity"	
				shopping_list_cost.append(500)
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="3"):
				shopping_list[cnt]=shopping_list[cnt]+" Ballaya"
				shopping_list_cost.append(600)
				cnt=cnt+1
				print("Successfully added to cart.")
		elif(user=="3"):   # sarees
			shopping_list.append(" Sarees")
			print("Choose the brand")
			print("1 Gadwal   RS.3000")
			print("2 uppada   RS.4500")
			print("3 Ballaya     RS.7000")
			print("4 Kanchipuram RS.6000")
			user=input()
			if(user=="1"):
				shopping_list[cnt]=shopping_list[cnt]+" Gadwal"	
				shopping_list_cost.append(3000)
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="2"):
				shopping_list[cnt]=shopping_list[cnt]+" Uppada"	
				shopping_list_cost.append(4500)
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="3"):
				shopping_list[cnt]=shopping_list[cnt]+" Ballaya"
				shopping_list_cost.append(7000)
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="4"):
				shopping_list[cnt]=shopping_list[cnt]+" Kanchipuram"
				shopping_list_cost.append(6000)
				cnt=cnt+1
				print("Successfully added to cart.")
		elif(user=="4"):   # tops
			f=0
			shopping_list.append("Tops")
			print("select the size( S,L,M,XL,XXL )")
			print("******************************************************************************************************************************************")
			print("******************************************************************************************************************************************")
			user=input().lower()
			if(user=="s"):
				shopping_list[cnt]=shopping_list[cnt]+" S"
				f=1
				gst=50
			elif(user=="l"):
				shopping_list[cnt]=shopping_list[cnt]+" L"	
				f=1
				gst=100
			elif(user=="m"):
				shopping_list[cnt]=shopping_list[cnt]+" M"
				f=1
				gst=150
			elif(user=="xl"):
				shopping_list[cnt]=shopping_list[cnt]+" XL"	
				f=1
				gst=200
			elif(user=="xxl"):
				shopping_list[cnt]=shopping_list[cnt]+" XXL"	
				f=1
				gst=250
			else:
				shopping_list.pop(cnt)
			if(f==0):
				shopping_list.pop(cnt)
			if(f==1):
				print("Choose the brand")
				print("1 Prisma    RS."+str(gst+150))
				print("2 Lyra     RS."+str(gst+200))
				print("3 Ballaya     RS."+str(gst+300))
				print("4 Fasaaak   RS."+str(gst+550))
				user=input()	
				if(user=="1"):
					shopping_list[cnt]=shopping_list[cnt]+" Prisma"	
					shopping_list_cost.append(gst+150)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="2"):
					shopping_list[cnt]=shopping_list[cnt]+" Lyra"	
					shopping_list_cost.append(gst+200)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="3"):
					shopping_list[cnt]=shopping_list[cnt]+" Ballaya"
					shopping_list_cost.append(gst+300)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="4"):
					shopping_list[cnt]=shopping_list[cnt]+" Fasaaak"
					shopping_list_cost.append(gst+550)
					cnt=cnt+1
					print("Successfully added to cart.")
				else:
					shopping_list.pop(cnt)
		user=""
		print("If you want to continue shopping  press 'Enter' .\n To exit press '0'   "  )
		e=input()
		if(e=="0"):
			z=0
		else:
			z=1
		for i in range(10):
			for j in range(10):
				print()
		print("******************************************************************************************************************************************")
		print("******************************************************************************************************************************************")	
	elif(user=="3"):  # mobiles and laptops ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		print("1 Mobiles")
		print("2 Laptops")
		print("******************************************************************************************************************************************")
		print("******************************************************************************************************************************************")			
		user=input()
		if(user=="1"):
			print("1 MI phone")
			print("2 Apple iphone")
			print("3 Oneplus")
			print("4 Samsung Galaxy")
			print("******************************************************************************************************************************************")
			print("******************************************************************************************************************************************")		
			user=input()
			if(user=="1"):   # mi phone
				print("1 Redmi 5                          RS.7999")
				print("2 Redmi Note 5                 RS.12999")
				print("3 Redmi Note 5 Pro          RS.16999")
				print("4 Mi mix                              RS.22999")
				print("5 Pocophone                     RS.29999")
				print("******************************************************************************************************************************************")
				print("******************************************************************************************************************************************")	
				user=input()
				if(user=="1"):
					shopping_list.append("Redmi 5")
					shopping_list_cost.append(7999)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="2"):
					shopping_list.append("Redmi Note 5")
					shopping_list_cost.append(12999)	
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="3"):
					shopping_list.append("Redmi Note 5 Pro")
					shopping_list_cost.append(16999)		
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="4"):
					shopping_list.append("Mi mix")
					shopping_list_cost.append(22999)		
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="5"):
					shopping_list.append("Pocophone")
					shopping_list_cost.append(29999)					
					cnt=cnt+1
					print("Successfully added to cart.")
			elif(user=="2"):   #  iphone
				print("1 Iphone 7                     RS.49999")
				print("2 Iphone 8                     RS.71999")
				print("3 Iphone X                     RS.90999")
				print("4 Iphone XS                   RS.100999")
				print("5 Iphone X Max              RS.119999")
				print("******************************************************************************************************************************************")
				print("******************************************************************************************************************************************")	
				user=input()
				if(user=="1"):
					shopping_list.append("Iphone 7")
					shopping_list_cost.append(49999)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="2"):
					shopping_list.append("Iphone 8")
					shopping_list_cost.append(71999)	
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="3"):
					shopping_list.append("Iphone X")
					shopping_list_cost.append(90999)	
					cnt=cnt+1
					print("Successfully added to cart.")	
				elif(user=="4"):
					shopping_list.append("Iphone XS")
					shopping_list_cost.append(100999)	
					cnt=cnt+1	
					print("Successfully added to cart.")
				elif(user=="5"):
					shopping_list.append("Iphone X Max")
					shopping_list_cost.append(119999)
					cnt=cnt+1
					print("Successfully added to cart.")
			elif(user=="3"):   #oneplus
				print("1  Oneplus  3          RS.15999")
				print("2  Oneplus 5           RS.22999")
				print("3  Oneplus 5t           RS.29999")
				print("4  Oneplus 6             RS.32999")
				print("5   Oneplus 6t         RS.39999")
				print("******************************************************************************************************************************************")
				print("******************************************************************************************************************************************")	
				user=input()
				if(user=="1"):
					shopping_list.append(" Oneplus 3 ")
					shopping_list_cost.append(15999)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="2"):
					shopping_list.append(" Oneplus 5 ")
					shopping_list_cost.append(22999)	
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="3"):
					shopping_list.append(" Oneplus 5t  ")
					shopping_list_cost.append(29999)		
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="4"):
					shopping_list.append(" Oneplus 6 ")
					shopping_list_cost.append(32999)	
					cnt=cnt+1	
					print("Successfully added to cart.")
				elif(user=="5"):
					shopping_list.append(" Oneplus 6t ")
					shopping_list_cost.append(39999)
					cnt=cnt+1
					print("Successfully added to cart.")
			elif(user=="4"):     #samsung
				print("1 Samsung Galaxy Note 9      RS.68999")
				print("2 Galaxy S9                               RS.57999")
				print("3 Galaxy A7                               RS.23999")
				print("******************************************************************************************************************************************")
				print("******************************************************************************************************************************************")					
				user=input()
				if(user=="1"):
					shopping_list.append(" Galaxy Note 9")
					shopping_list_cost.append(68999)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="2"):
					shopping_list.append(" Galaxy S9")
					shopping_list_cost.append(57999)	
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="3"):
					shopping_list.append(" Galaxy A7")
					shopping_list_cost.append(23999)		
					cnt=cnt+1
					print("Successfully added to cart.")
			user=""
		elif(user=="2"):   #laptops
			print("1 HP                                                         RS.48999")
			print("2 Dell                                                       RS.57999")
			print("3 Asus                                                        RS.63999")
			print("4 Apple MacBook pro                             RS.123999")
			print("******************************************************************************************************************************************")
			print("******************************************************************************************************************************************")		
			user=input()
			if(user=="1"):
				shopping_list.append(" HP Laptop")
				shopping_list_cost.append(48999)
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="2"):
				shopping_list.append(" Dell Laptop")
				shopping_list_cost.append(57999)	
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="3"):
				shopping_list.append(" Asus Laptop")
				shopping_list_cost.append(63999)				
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="4"):
				shopping_list.append(" Apple MacBook Laptop")
				shopping_list_cost.append(123999)			
				cnt=cnt+1
				print("Successfully added to cart.")		
		user=""
		print("If you want to continue shopping  press 'Enter' .\n To exit press '0'   "  )
		e=input()
		if(e=="0"):
			z=0
		else:
			z=1
		for i in range(10):
			for j in range(10):
				print()
		print("******************************************************************************************************************************************")
		print("******************************************************************************************************************************************")	
	if(user=="4"):   #books -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		print("1 Wings of fire             RS.599")
		print("2 War and Peace        RS.399")
		print("3 1984                           RS.299")
		print("4 One Indian Girl          RS.359")
		print("5 Think and Grow up   RS.699")
		print("******************************************************************************************************************************************")
		print("******************************************************************************************************************************************")		
		user=input()
		if(user=="1"):
			shopping_list.append(" Wings Of fire")
			shopping_list_cost.append(599)
			cnt=cnt+1
			print("Successfully added to cart.")
		elif(user=="2"):
			shopping_list.append(" War and Peace")
			shopping_list_cost.append(399)
			cnt=cnt+1
			print("Successfully added to cart.")
		elif(user=="3"):
			shopping_list.append(" 1984")
			shopping_list_cost.append(299)
			cnt=cnt+1
			print("Successfully added to cart.")
		elif(user=="4"):
			shopping_list.append(" One Indian Girl")
			shopping_list_cost.append(359)
			cnt=cnt+1
			print("Successfully added to cart.")
		elif(user=="5"):
			shopping_list.append(" Think and Grow up")
			shopping_list_cost.append(599)
			cnt=cnt+1
			print("Successfully added to cart.")
		user=""
		print("If you want to continue shopping  press 'Enter' .\n To exit press '0'   "  )
		e=input()
		if(e=="0"):
			z=0
		else:
			z=1
		for i in range(10):
			for j in range(10):
				print()
		print("******************************************************************************************************************************************")
		print("******************************************************************************************************************************************")	
	elif(user=="5"):   #tv stick and echo  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		print("1 TV stick (limited edition)      RS.4999")
		print("2 Echo                                       RS.10999")
		print("******************************************************************************************************************************************")
		print("******************************************************************************************************************************************")		
		user=input()
		if(user=="1"):
			shopping_list.append(" TV stick")
			shopping_list_cost.append(4999)
			cnt=cnt+1
			print("Successfully added to cart.")
		elif(user=="2"):
			shopping_list.append(" Echo")
			shopping_list_cost.append(10999)
			cnt=cnt+1
			print("Successfully added to cart.")
		user=""
		print("If you want to continue shopping  press 'Enter' .\n To exit press '0'   "  )
		e=input()
		if(e=="0"):
			z=0
		else:
			z=1
		for i in range(10):
			for j in range(10):
				print()
		print("******************************************************************************************************************************************")
		print("******************************************************************************************************************************************")	


	elif(user=="6"):  # groceries  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		print(" 1 Karachi biscuits           RS.250  \n 2 Sunfeast Dark Fantasy           RS.40 \n 3 Lays           RS.20 \n 4 Kurkure           RS.10 \n 5 Ashirvad Salt           RS.20 \n 6 Olive oil           RS.500 \n 7 Honey           RS.100 \n 8 Jam           RS.60 \n 9 ThumpsUp           RS.90 \n 10 Red Label Tea           RS.55 \n 11 Maaza           RS.60 \n 12 Brizzer           RS.120 \n 13 Horlicks           RS.180 \n 14 Surf Excel           RS.90 \n 15 Maggi           RS.20  ")
		grocery=[" "," Karachi Biscuits"," Sunfeast Dark Fantasy "," Lays"," Kurkure "," Ashirvad Salt","Olive oil"," Honey"," Jam "," ThumpsUp"," Red Label Tea"," Maaza"," Brizzer"," Horlicks"," Surf Excel"," Maggi"]
		grocery_cost=[0,250,40,20,10,20,500,100,60,90,55,60,120,180,90,20]
		print("Select your product")
		user=input()
		e="1"
		if(int(user)<=15):
			print(grocery[int(user)])
			shopping_list.append(grocery[int(user)])
			shopping_list_cost.append(grocery_cost[int(user)])
			cnt=cnt+1
			print("Successfully added to cart.")		
			print("If you want to continue shopping  press 'Enter' .\n To exit press '0'   "  )
			e=input()
		else:
			print("Enter a valid item number")
		if(e=="0"):
			z=0
		else:
			z=1
		for i in range(10):
			for j in range(10):
				print()
		print("******************************************************************************************************************************************")
		print("******************************************************************************************************************************************")	
	elif(user=="0"):    #  this condition changes  z to '0'  so that the loop end , and then go to the payment section.
		print()
		z=0
	else:        #if the wrong key is pressed then go to main 
		for i in range(10):
			for j in range(10):
				print()	
		print("------------------- Please choose category ------------------")
t=0                                #   variable that enable the code to go to the payment section after removing of unwanted items from the cart  and also quit the code.
tcnt=cnt                                 #   a temporary variable that is used to store the count value
print("######  To see your items and proceed to payment  , Press 'Enter'")                   
print(" #######   To cancel you order ,Press '0' ")
print("##########   To remove any item , Press 'r'  ")
user1=input()
print("Loading....")
time.sleep(1)
for i in range(10):
	for j in range(10):
		print()	
if(user1=="0"):   #  directly exit from the program
	for i in range(cnt):           # to print  cart items 
		print(str(i+1)+"                "+str(shopping_list[i])+"                                                                 "+str(shopping_list_cost[i]))
		i=i+1
		time.sleep(0.2)
	print()
	print()
	print("Your total price")
	print(sum(shopping_list_cost))
	print("Total number of items in your cart = "+str(cnt))
	print("Press any key to remove items from your cart  and exit.")
	user=input()
	t=1
	if(t==1):
		print("loading......")
		time.sleep(2)
		print("Your cart is empty now")
		print("Thanks for shopping with us.   :)")
		exit()
	
elif(user1=="r"):      #remove unwanted items from the cart
	z=1        # a temporary variable that is used for executing the loop multiple times
	while(z!=0):               # if z=0 ,then loop stops or else it will continue.
		for i in range(tcnt):
			print(str(i+1)+"                "+str(shopping_list[i])+"                                                                 "+"RS."+str(shopping_list_cost[i]))                              #   printing the items in the cart
			i=i+1
		time.sleep(0.3)
		print("Please enter the serial number to be removed")
		user=input()               #     this input will remove the unwanted items from the list
		if(int(user)<=tcnt):	
			shopping_list.pop(int(user)-1)     #  removing  item name 
			shopping_list_cost.pop(int(user)-1)     #  removing the item price
			print("successfully removed.")
			print("To remove another item, Press 'r'  again")
			print("Else Press any key to continue for payment")
			user1=input()            #    asking the user whether he wants to remove any other item from the list
		else:
			print("To remove another item, Press 'r'  again")
			print("Else Press any key to continue for payment")
			user1=input()            #    asking the user whether he wants to remove any other item from the list
		if(user1=="r"):              #    condition that runs the loop
			print("loading......")
			time.sleep(2)
			z=1	
			tcnt=tcnt-1
		else :                        # if user gives ay other input then this loop ends
			z=0             
			t=1
			tcnt=tcnt-1
else:                   #  if the user simply presses enter then it will direct to payment code.
	t=1
if(t!=0):         #   above we defined 't' to enter this condition 
	bank=""           #      stores bank name
	address=""           #     to store delivery address 
	dis=0     #   a variable to store discount value 
	for i in range(10):     
		for j in range(10):
			print()
	print("loading......")
	time.sleep(2)
	for i in range(10):   
		for j in range(10):
			print()
	i=0
	for i in range(tcnt):
		print(str(i+1)+"                "+str(shopping_list[i])+"                                                                 "+"RS."+str(shopping_list_cost[i]))                                              #  to finally display the items in the cart
		i=i+1
	print()
	print()
	print("Your total price")
	fp=sum(shopping_list_cost)
	print(fp)
	print("Total number of items in your cart = "+str(tcnt))           #   total number of items in user cart
	print("Since this is your first order , you are provided with a coupon 'FIRSTorder'  .\n ENTER THE CODE to get a discount of 4% on your products.\n Else press any  key to proceed for payment.")        #    a coupon code that gives 4% discount to the user
	user=input()
	for i in range(10):     
		for j in range(10):
			print()
	t=0
	if(user=="FIRSTorder"):       #      comparing  it with coupon code
		print("Final amount ="+str(fp))
		dis=fp*(4/100)
		print("discount         =  -"+str(dis))
		print()
		time.sleep(2)
		print("Final amount (After discount)  ="+str(fp-dis))      #  final amount that should be paid by the customer
		print("Hurrah!!!! you got a discount of 4% on your products")
		print("******************************************************************************************************************************************")
		print("******************************************************************************************************************************************")	
	else:             
		print("Final amount ="+str(fp))
		print("******************************************************************************************************************************************")
		print("******************************************************************************************************************************************")	
	time.sleep(1.5)
	print("Enter the captcha(only one chance is given ) ")  
	time.sleep(3)               
	img = Image.open('cap1.png')
	img.show()                  # here captcha is displayed
	user=input()
	print("Please wait.....")
	time.sleep(3)
	if(user=="W68HP"):                # if the captcha is corrent then this condition is satistifed
		for i in range(10):     
			for j in range(10):
				print()		
		print("************************ PAYMENT *************************")		
		print("Please enter your delivery address  (House number,colony,city,state,pincode)")
		time.sleep(3)
		address=input()	
		print("Please select the type of payment")
		print("1 Net banking")
		print("2 Credit card")                                    
		print("3 Cash on delivery")
		print("Press any key to exit payment ")
		user=input()
		if(user=="1" or user=="2"):               #  both net banking and credit card are given the same type of code
			print("loading......")
			time.sleep(2)
			print("Please enter your Bank Name")
			bank=input().upper()                   #   storing the bank name in uppercase
			print("loading......")
			time.sleep(2)
			print("Please enter your Password")
			use=input()                  #   to give a banking feeling to user password is asked			
			if(user=="2"):      #   credit card payment
				print("Enter 16 Digit number")
				user=input()
				print("Enter CVV")
				user=input()
				print("Enter Expire date")
				user=input()
			for i in range(10):     
				for j in range(10):
					print()
			print(bank+"  BANK")
			print("Net amount to be paid: RS."+str(fp))
			print()
			time.sleep(2)
			print("Feedback about the application:",end="")                # asking feedback from the user about the application 
			user=input()
			print("\nPress 'n' to cancel payment. \n Press 'enter' to preceed for payment")             
			user=input()            # again asking the user whether he want to quit or not 
			print("loading......")
			time.sleep(2)
			if(user=='n'):              #   if yes below statements are displayed
				print("Your payment has been cancelled . Your items in your cart are also removed .")              
				print("Your cart is empty now")
				print("Thanks for shopping with us.   :)")
			else:	
				print("Your payment is successful.")
				print("Your order will deliver to :")
				print(address)
				print("In the next 5 days .\n Thanks for shopping with us.   :)")
		elif(user=="3"):               #  if cash on delivery is chosen below statements are executed
			print("Your order will deliver to :")
			print(address)
			print("In the next 5 days .\n Thanks for shopping with us.  :) ")
		else:
			print("Your cart is empty now")
			print("Thanks for shopping with us.   :)")
	else:
		for i in range(10):   
			for j in range(10):
				print()
		print()
		print("Wrong captcha.")
		print("Your payment has been cancelled . Your items in your cart are also removed .")
		print("Your cart is empty now")
		print("Thanks for shopping with us.   :)")

#   DONE  :)

