#!/usr/bin/env python

import math
from subprocess import call
import time

def c():
	call('cls',shell=True)
def cc(sec):
	while sec:
		m,s = divmod(sec,60)
		time.sleep(1)
		sec-= 1
#color
r = "\033[0;49;31m"
rb = "\033[7;49;31m"
br = "\033[1;49;31m"
g = "\033[0;49;32m"
gb = "\033[7;49;32m"
bg = "\033[1;49;32m"
b = "\033[0;49;96m"
bb = "\033[7;49;96m"
p = "\033[0;49;94m"
pb = "\033[7;49;94m"
e = "\033[0m"
#variables 
len = f"{bg}[L]{b} length{e} "
wid = f"{bg}[W]{b} width{e} "
hei = f"{bg}[H]{b} height{e} "
dia = f"{bg}[D]{b} diagonal{e} "
ar = f"{bg}[A]{b} area{e} "
vol = f"{bg}[V]{b} volume{e} "
#txt variables
op = f'''{r}
      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
   ___█─▄▄─█▄─▄▄─█─▄─▄─█▄─▄█─▄▄─█▄─▀█▄─▄█─▄▄▄▄█___
   ___█─██─██─▄▄▄███─████─██─██─██─█▄▀─██▄▄▄▄─█___
      █▄▄▄▄█▄▄▄████▄▄▄██▄▄▄█▄▄▄▄█▄▄▄██▄▄█▄▄▄▄▄█'''
opttxt = f"{op}\n\n\t\t{vol}{b}of a cuboid.\n\t\t{ar}{b}of a cuboid.\n\t\t{dia}{b}of a cuboid.\n\t\t{len}{b}of a cuboid.\n\t\t{wid}{b}of a cuboid.\n\t\t{hei}{b}of a cuboid.\n\n{br}INPUT > {e}"

prs0 = f"\t\t{gb}CALCULATING {e}"
prs1 = f"{gb} OF A CUBOID.{e}\n\t\t   {pb}PLEASE ENTER THE VALUES{e}"

et = f'''{br}\n\t\t\t*TERMINATING*{e}'''

#function
	#volume
def v():
	c()
	print(f"\n{prs0}{gb}[V] VOLUME{e}{prs1}")
	l = float(input(len))
	w = float(input(wid))
	h = float(input(hei))
	fvol = (l*w*h)
	print(f"\n{br}[+]{b} V = {l}×{w}×{h}\n{vol}= {bb}{fvol}{e}")
	#area
def a():
	c()
	print(f"\n{prs0}{gb}[A] AREA{e}{prs1}")
	l = float(input(f"{len} >"))
	w = float(input(f"{wid} >"))
	h = float(input(f"{hei} >"))
	far = 2*(l*w + w*h + h*l)
	print(f"\n{br}[+]{b} A = 2({l}×{w}+{w}×{h}+{h}×{l})\n{ar}= {bb}{far}{e}")
	#diagonal
def d():
	c()
	print(f"\n{prs0}{gb}[D] DIAGONAL{e}{prs1}")
	l = float(input(len))
	w = float(input(wid))
	h = float(input(hei))
	fdia = math.sqrt(l*l + w*w + h*h)
	print(f"\n{br}[+]{b} D = √{l}²+{w}²+{h}²\n{dia}= {bb}{fdia}{e}")
	#length
def l():
	c()
	print(f"{prs0}{gb}[L]LENGTH{e}{prs1}")
	w = float(input(wid))
	h = float(input(hei))
	v = float(input(vol))
	flen = v/(w*h)
	print(f"\n{br}[+]{b} L = {v}/{w}×{h}\n{len}= {bb}{flen}{e}")
	#width
def w():
	c()
	print(f"{prs0}{gb}[W]WIDHT{e}{prs1}")
	l = float(input(len))
	h = float(input(hei))
	v = float(input(vol))
	fwid = v/(l*h)
	print(f"\n{br}[+]{b} W = {v}/{l}×{h}\n{wid}= {bb}{fwid}{e}")
	#height
def h():
	c()
	print(f"{prs0}{gb}[H]HEIGHT{e}{prs1}")
	l = float(input(len))
	w = float(input(wid))
	v = float(input(vol))
	fhei = v/(l*w)
	print(f"\n{br}[+]{b} H = {v}/{l}×{w}\n{hei}= {bb}{fhei}{e}")
	
def io2():
	i = input(br+"> "+e).lower()
	if i == "v":
		v()
		io2()
	elif i == "a":
		a()
		io2()
	elif i == "d":
		d()
		io2()
	elif i == "l":
		l()
		io2()
	elif i == "w":
		w()
		io2()
	elif i == "h":
		h()
		io2()
	elif i == "exit":
		c()

while True:
	try:
		c()
		inopt = input(opttxt).lower()
		#volume
		if inopt == "v":
			v()
			io2()
		#area	
		elif inopt == "a":
			a()
			io2()
		#diagonal		
		elif inopt == "d":
			d()
			io2()
		#length	
		elif inopt == "l":
			l()
			io2()
		#width		
		elif inopt == "w":
			w()
			io2()
		#height	
		elif inopt == "h":
			h()
			io2()
			
		elif inopt == "exit":
			print(et)
			cc(2)
			c()
			break
		
		elif inopt == " ":
			print(f"{br}ERROR! input cannot be blank{e}")
			cc(1)
		else:
			print(f"{br}ERROR! input invalid{e}")
			cc(1)
	except:
		print(f"{br}ERROR!{e}")
		cc(1)