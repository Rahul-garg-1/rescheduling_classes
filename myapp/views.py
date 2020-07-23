from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.utils import timezone
import datetime
import calendar
from datetime import datetime,date
from myapp.abc import findDay 
from django.views.generic import ListView
from myapp.models import t8_9,t9_10,t10_11,t11_12,t12_1,t1_2,t2_3,t3_4,t4_5,update
from django.contrib import messages
# Create your views here.

# def index(request):
# 	return render(request,'myapp/index.html')
@login_required
def block(request):
	return render(request,'myapp/blocks.html')
@login_required
def build1(request):
	if request.method=='POST':
		if 'NAB' in request.POST:
			blockis='NAB'
		if 'Electrical' in request.POST:
			blockis='Electrical'
		if 'Production' in request.POST:
			blockis='Production'
		if 'Metta' in request.POST:
			blockis='Metta'
		if 'Aero' in request.POST:
			blockis='Aero'
		if 'Audi' in request.POST:
			blockis='Audi'
		block={'block_is':blockis}	

		return render(request,'myapp/build1.html',context=block)
@login_required
def booking(request):
	if request.method=='POST':
		day=request.POST.get('day_is')
		time=request.POST.get('time_is')
		date=request.POST.get('date_is')
		hall=request.POST.get('hall_is')
		room=request.POST.get('lecture_hall')
		blockname=request.POST.get('block_is')
		buttonis=request.POST.get('button1')
		search_type='exact'
		search_string=day+'__'+search_type
		global u
		status='empty'
		if(buttonis=='Book'):
			status=u
		if(time=='1'):
			get_name=t8_9.objects.filter(halls__exact=room).update(**{day:status})
		elif(time=='2'):
			get_name=t9_10.objects.filter(halls__exact=room).update(**{day:status})
		elif(time=='3'):
			get_name=t10_11.objects.filter(halls__exact=room).update(**{day:status})
		elif(time=='4'):
			get_name=t11_12.objects.filter(halls__exact=room).update(**{day:status})
		elif(time=='5'):
			get_name=t12_1.objects.filter(halls__exact=room).update(**{day:status})
		elif(time=='6'):
			get_name=t1_2.objects.filter(halls__exact=room).update(**{day:status})
		elif(time=='7'):
			get_name=t2_3.objects.filter(halls__exact=room).update(**{day:status})
		elif(time=='8'):
			get_name=t3_4.objects.filter(halls__exact=room).update(**{day:status})
		elif(time=='9'):
			get_name=t4_5.objects.filter(halls__exact=room).update(**{day:status})
		
			
		block={'block_is':blockname,'abc':True}
		messages.success(request,"You have Successfully processed your request")
		return render(request,'myapp/build1.html',context=block)

			









@login_required
def lecture(request):
	# def findDay(date): 
	# 	day, month, year = (int(i) for i in date.split('/'))     
	# 	born = datetime.date(year, month, day) 
	# 	return born.strftime("%A")
	if request.method=='POST':	
		global u
		if 'L' in request.POST or 'L_cancel' in request.POST:

			date=request.POST.get('date1')
			time=request.POST.get('time1')
			blockname=request.POST.get('blockname')


			date=str(date)
			block={'block_is':blockname,'abc':False}
			if(date==""):
				messages.error(request,"You can't leave the date field empty!!")
				return render(request,'myapp/build1.html',context=block)
			date_format='%Y-%m-%d'
			df1='%m/%d/%Y'
			a = datetime.strptime(str(datetime.now().date()), date_format)
			b=datetime.strptime(str(date),df1)
			delta=b-a
			day1=(findDay(date))
			day1=day1.lower()
			hall='L'
			
			if(delta.days<0):
				messages.error(request,"You can't Book/Cancel the class in past")
				return render(request,'myapp/build1.html',context=block)
			elif(delta.days>=7):
				messages.error(request,"You are thinking of too far.You can Book/Cancel classes of only one week")
				return render(request,'myapp/build1.html',context=block)
			elif(day1=='saturday' or day1=='sunday'):
				messages.error(request,"It's your holiday,enjoy!!!")
				return render(request,'myapp/build1.html',context=block)
			
			else:
				date1=update.objects.filter(day__exact=day1)
				c='abc'
				for j in date1:
					c=datetime.strptime(str(j.date),df1)
				diff=b-c
				if(diff.days!=0):
					if(day1=='tuesday'):
						original=t8_9.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t9_10.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t10_11.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t11_12.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t12_1.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t1_2.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t2_3.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t3_4.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t4_5.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
					elif (day1=='monday'):
						original=t8_9.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t9_10.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t10_11.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t11_12.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t12_1.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t1_2.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t2_3.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t3_4.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t4_5.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
					elif (day1=='wednesday'):
						original=t8_9.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t9_10.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t10_11.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t11_12.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t12_1.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t1_2.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t2_3.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t3_4.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t4_5.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])	
					elif (day1=='thursday'):
						original=t8_9.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t9_10.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t10_11.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t11_12.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t12_1.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t1_2.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t2_3.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t3_4.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t4_5.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])	
					elif (day1=='friday'):
						original=t8_9.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t9_10.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t10_11.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t11_12.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t12_1.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t1_2.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t2_3.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t3_4.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t4_5.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])

					update.objects.filter(day__exact=day1).update(date=date)									







			
					# day, month, year = (int(i) for i in date.split('/'))     
					# day1 = datetime.date(year, month, day) 
					# day1=day1.strftime("%A")
				
				status='empty'
				button1='Book'
				if 'L_cancel' in request.POST:
					status=u
					button1='Cancel'
				day_is=day1
				search_type='exact'
				search_string=day1+'__'+search_type
				if(time=='1'):
					lecture_halls=t8_9.objects.filter(types__exact='L',block__exact=blockname,**{search_string:status})
				elif(time=='2'):
					lecture_halls=t9_10.objects.filter(types__exact='L',block__exact=blockname,**{search_string:status})
				elif(time=='3'):
					lecture_halls=t10_11.objects.filter(types__exact='L',block__exact=blockname,**{search_string:status})
				elif(time=='4'):
					lecture_halls=t11_12.objects.filter(types__exact='L',block__exact=blockname,**{search_string:status})
				elif(time=='5'):
					lecture_halls=t12_1.objects.filter(types__exact='L',block__exact=blockname,**{search_string:status})
				elif(time=='6'):
					lecture_halls=t1_2.objects.filter(types__exact='L',block__exact=blockname,**{search_string:status})
				elif(time=='7'):
					lecture_halls=t2_3.objects.filter(types__exact='L',block__exact=blockname,**{search_string:status})
				elif(time=='8'):
					lecture_halls=t3_4.objects.filter(types__exact='L',block__exact=blockname,**{search_string:status})
				elif(time=='9'):
					lecture_halls=t4_5.objects.filter(types__exact='L',block__exact=blockname,**{search_string:status})
				lecture_dict={'lectures':lecture_halls,'time':time,'day':day1,'halls':hall,'dates':date,'blocks':blockname,'button':button1}
				return render(request,'myapp/lecture.html',context=lecture_dict)
		elif 'A' in request.POST or 'A_cancel' in request.POST:
			date=request.POST.get('date2')
			time=request.POST.get('time2')
			blockname=request.POST.get('blockname')

			date=str(date)
			block={'block_is':blockname,'abc':False}
			if(date==""):
				messages.error(request,"You can't leave the date field empty!!")
				return render(request,'myapp/build1.html',context=block)
			date_format='%Y-%m-%d'
			df1='%m/%d/%Y'
			a = datetime.strptime(str(datetime.now().date()), date_format)
			b=datetime.strptime(str(date),df1)
			delta=b-a
			day1=(findDay(date))
			day1=day1.lower()
			hall='A'
			
			if(delta.days<0):
				messages.error(request,"You can't Book/Cancel the class in past")
				return render(request,'myapp/build1.html',context=block)
			elif(delta.days>=7):
				messages.error(request,"You are thinking of too far.You can Book/Cancel classes of only one week")
				return render(request,'myapp/build1.html',context=block)
			elif(day1=='saturday' or day1=='sunday'):
				messages.error(request,"It's your holiday,enjoy!!!")
				return render(request,'myapp/build1.html',context=block)
			
			else:
				date1=update.objects.filter(day__exact=day1)
				c='abc'
				for j in date1:
					c=datetime.strptime(str(j.date),df1)
				diff=b-c
				if(diff.days!=0):
					if(day1=='tuesday'):
						original=t8_9.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t9_10.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t10_11.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t11_12.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t12_1.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t1_2.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t2_3.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t3_4.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t4_5.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
					elif (day1=='monday'):
						original=t8_9.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t9_10.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t10_11.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t11_12.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t12_1.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t1_2.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t2_3.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t3_4.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t4_5.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
					elif (day1=='wednesday'):
						original=t8_9.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t9_10.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t10_11.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t11_12.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t12_1.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t1_2.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t2_3.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t3_4.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t4_5.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])	
					elif (day1=='thursday'):
						original=t8_9.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t9_10.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t10_11.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t11_12.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t12_1.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t1_2.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t2_3.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t3_4.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t4_5.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])	
					elif (day1=='friday'):
						original=t8_9.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t9_10.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t10_11.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t11_12.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t12_1.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t1_2.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t2_3.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t3_4.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t4_5.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])

					update.objects.filter(day__exact=day1).update(date=date)		
				
				status='empty'
				button1='Book'
				if 'A_cancel' in request.POST:
					status=u 
					button1='Cancel'
				search_type='exact'
				search_string=day1+'__'+search_type
				if(time=='1'):
					labs=t8_9.objects.filter(types__exact='A',block__exact=blockname,**{search_string:status})
				elif(time=='2'):
					labs=t9_10.objects.filter(types__exact='A',block__exact=blockname,**{search_string:status})
				elif(time=='3'):
					labs=t10_11.objects.filter(types__exact='A',block__exact=blockname,**{search_string:status})
				elif(time=='4'):
					labs=t11_12.objects.filter(types__exact='A',block__exact=blockname,**{search_string:status})
				elif(time=='5'):
					labs=t12_1.objects.filter(types__exact='A',block__exact=blockname,**{search_string:status})
				elif(time=='6'):
					labs=t1_2.objects.filter(types__exact='A',block__exact=blockname,**{search_string:status})
				elif(time=='7'):
					labs=t2_3.objects.filter(types__exact='A',block__exact=blockname,**{search_string:status})
				elif(time=='8'):
					labs=t3_4.objects.filter(types__exact='A',block__exact=blockname,**{search_string:status})
				elif(time=='9'):
					labs=t4_5.objects.filter(types__exact='A',block__exact=blockname,**{search_string:status})
				lab_dict={'lab':labs,'time':time,'day':day1,'halls':hall,'dates':date,'blocks':blockname,'button':button1}
				return render(request,'myapp/lab.html',context=lab_dict)
		elif 'T' in request.POST or 'T_cancel' in request.POST:
			date=request.POST.get('date3')
			time=request.POST.get('time3')
			blockname=request.POST.get('blockname')


			date=str(date)
			block={'block_is':blockname,'abc':False}
			if(date==""):
				messages.error(request,"You can't leave the date field empty!!")
				return render(request,'myapp/build1.html',context=block)

			date_format='%Y-%m-%d'
			df1='%m/%d/%Y'
			a = datetime.strptime(str(datetime.now().date()), date_format)
			b=datetime.strptime(str(date),df1)
			delta=b-a
			day1=(findDay(date))
			day1=day1.lower()
			hall='T'
			
			if(delta.days<0):
				messages.error(request,"You can't Book/Cancel the class in past")
				return render(request,'myapp/build1.html',context=block)
			elif(delta.days>=7):
				messages.error(request,"You are thinking of too far.You can Book/Cancel classes of only one week")
				return render(request,'myapp/build1.html',context=block)
			elif(day1=='saturday' or day1=='sunday'):
				messages.error(request,"It's your holiday,enjoy!!!")
				return render(request,'myapp/build1.html',context=block)
		
			# if(day1=='saturday' or day1=='sunday' or delta.days>=7 or delta.days<0):
			# 	return HttpResponse("Pehli fursat me vapis nikal lawde")
			else:
				date1=update.objects.filter(day__exact=day1)
				c='abc'
				for j in date1:
					c=datetime.strptime(str(j.date),df1)
				diff=b-c
				if(diff.days!=0):
					if(day1=='tuesday'):
						original=t8_9.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t9_10.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t10_11.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t11_12.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t12_1.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t1_2.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t2_3.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t3_4.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
						original=t4_5.objects.all()
						for i in original:
							i.tuesday=i.tuesday_copy
							i.save(update_fields=['tuesday'])
					elif (day1=='monday'):
						original=t8_9.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t9_10.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t10_11.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t11_12.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t12_1.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t1_2.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t2_3.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t3_4.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
						original=t4_5.objects.all()
						for i in original:
							i.monday=i.monday_copy
							i.save(update_fields=['monday'])
					elif (day1=='wednesday'):
						original=t8_9.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t9_10.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t10_11.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t11_12.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t12_1.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t1_2.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t2_3.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t3_4.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])
						original=t4_5.objects.all()
						for i in original:
							i.wednesday=i.wednesday_copy
							i.save(update_fields=['wednesday'])	
					elif (day1=='thursday'):
						original=t8_9.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t9_10.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t10_11.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t11_12.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t12_1.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t1_2.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t2_3.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t3_4.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])
						original=t4_5.objects.all()
						for i in original:
							i.thursday=i.thursday_copy
							i.save(update_fields=['thursday'])	
					elif (day1=='friday'):
						original=t8_9.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t9_10.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t10_11.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t11_12.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t12_1.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t1_2.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t2_3.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t3_4.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])
						original=t4_5.objects.all()
						for i in original:
							i.friday=i.friday_copy
							i.save(update_fields=['friday'])

					update.objects.filter(day__exact=day1).update(date=date)		
				
				status='empty'
				button1='Book'
				if 'T_cancel' in request.POST:
					status=u
					button1='Cancel'
				search_type='exact'
				search_string=day1+'__'+search_type
				if(time=='1'):
					tuts=t8_9.objects.filter(types__exact='T',block__exact=blockname,**{search_string:status})
				elif(time=='2'):
					tuts=t9_10.objects.filter(types__exact='T',block__exact=blockname,**{search_string:status})
				elif(time=='3'):
					tuts=t10_11.objects.filter(types__exact='T',block__exact=blockname,**{search_string:status})
				elif(time=='4'):
					tuts=t11_12.objects.filter(types__exact='T',block__exact=blockname,**{search_string:status})
				elif(time=='5'):
					tuts=t12_1.objects.filter(types__exact='T',block__exact=blockname,**{search_string:status})
				elif(time=='6'):
					tuts=t1_2.objects.filter(types__exact='T',block__exact=blockname,**{search_string:status})
				elif(time=='7'):
					tuts=t2_3.objects.filter(types__exact='T',block__exact=blockname,**{search_string:status})
				elif(time=='8'):
					tuts=t3_4.objects.filter(types__exact='T',block__exact=blockname,**{search_string:status})
				elif(time=='9'):
					tuts=t4_5.objects.filter(types__exact='T',block__exact=blockname,**{search_string:status})
				
				tut_dict={'tut':tuts,'time':time,'day':day1,'halls':hall,'dates':date,'blocks':blockname,'button':button1}
				return render(request,'myapp/tuts.html',context=tut_dict)

				
								
  
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('user_login'))

def user_login(request):

	if request.method=='POST':
		username=request.POST.get('Username')
		password=request.POST.get('Password')
		

		user=authenticate(username=username, password=password)
		global u
		u=username

		if user:
			

			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('block')

		else:
			messages.error(request,"Invalid Login Details")
			return render(request,'myapp/index.html')

	else:
		return render(request,'myapp/index.html')
# def labs(request):
# 	if request.method=='POST':
		
# 		date=request.POST.get('date')
# 		time=request.POST.get('time')

# 		date=str(date)
# 		date_format='%Y-%m-%d'
# 		df1='%m/%d/%Y'
# 		a = datetime.strptime(str(datetime.now().date()), date_format)
# 		b=datetime.strptime(str(date),df1)
# 		delta=b-a
# 		day1=(findDay(date))
# 		day1=day1.lower()
# 		if(day1=='saturday' or day1=='sunday' or delta.days>=7 or delta.days<0):
# 			return HttpResponse("Pehli fursat me vapis nikal lawde")
# 		else:
# 			search_type='exact'
# 			search_string=day1+'__'+search_type
# 			if(time=='1'):
# 				labs=t8_9.objects.filter(types__exact='A',block__exact='NAB',**{search_string:0})
# 			lab_dict={'lab':labs}

# 		return render(request,'myapp/lab.html',context=lab_dict)
	
				

# def tuts(request):
# 	if request.method=='POST':
# 		date=request.POST.get('date')
# 		time=request.POST.get('time')

# 		date=str(date)
# 		date_format='%Y-%m-%d'
# 		df1='%m/%d/%Y'
# 		a = datetime.strptime(str(datetime.now().date()), date_format)
# 		b=datetime.strptime(str(date),df1)
# 		delta=b-a
# 		day1=(findDay(date))
# 		day1=day1.lower()
# 		if(day1=='saturday' or day1=='sunday' or delta.days>=7 or delta.days<0):
# 			return HttpResponse("Pehli fursat me vapis nikal lawde")
# 		else:
# 			search_type='exact'
# 			search_string=day1+'__'+search_type
# 			if(time=='1'):
# 				tuts=t8_9.objects.filter(types__exact='T',block__exact='NAB',**{search_string:0})
# 			tut_dict={'tut':tuts}

# 		return render(request,'myapp/tuts.html',context=tut_dict)
