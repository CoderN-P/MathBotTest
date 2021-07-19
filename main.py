import discord
import os
import requests
import json
import keep_alive
from math import sqrt
from time import perf_counter
from dotenv import load_dotenv()
load_dotenv()
def perfect_square(limit):  
    accumulation_list = [1]
    index, increment = 0, 3
    while accumulation_list[-1] + increment <= limit:
        accumulation_list.append(accumulation_list[index] + increment)
        index += 1 
        increment = 2 * index + 3
    return accumulation_list


def reduced_sqrt(n):
    """Print most reduced form of square root of n"""

    if n < 0:
        print('Negative input')
        return

    if sqrt(n).is_integer():
        print(int(sqrt(n)))
        return 

    # Find perfect squares that are factors of n
    factors = [square for square in perfect_square(n/2) if n % square == 0 and square > 1]
    if len(factors) == 0:
        return f'\u221A{n}' # Square root is irreducible
    else:
        a = int(sqrt(max(factors))) # Coefficient
        b = int(n / max(factors)) # Argument of the square root
        return f'{a}\u221A{b}' # Reduced square root

client = discord.Client()
keep_alive.keep_alive()
@client.event


async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  
    if message.author == client.user:
        return

    if message.content.startswith('hello math bot'):
      await message.channel.send("Hello! I am math bot")


    if message.content.startswith('$calc '):
            a = str(message.content)
            e = a.split(' ')
            l = list(e)
            
            l.pop(0)

            for x, y in enumerate(l):
              if '^' in y:
                l[x] = y.replace('^', '**')

              if '|' in y:
                l[x] = y.replace('|', '**0.5')

          
            
              
            
            try:
              thing = ' '.join(l)
              a = eval(thing)
            except: 
              await message.channel.send("Sorry your command was not valid. This could have been caused by typing a letter in the numbers or typing the numbers more than 1 space apart")
              
              return

            await message.channel.send(a)
    

    if message.content.startswith('$rad '):
      a1 = message.content
      e1 = a1.split(' ')
      l1 = list(e1)
      l1.pop(0)
      items = []
      for i in l1:
        items.append(reduced_sqrt(int(i)))


      result = ', '.join(items)

      await message.channel.send(result)

    
  


    

    if message.content.startswith('$jokes/general'):
          def jokes(f):
    
              data = requests.get(f)
              tt = json.loads(data.text)
              return tt

          f = r"https://official-joke-api.appspot.com/jokes/general/random"
          a = jokes(f)

          

          for i in (a):
            await message.channel.send(i["setup"])
            await message.channel.send(i["punchline"])

    if message.content.startswith('$jokes/programming'):
          def jokes(f):
    
              data = requests.get(f)
              tt = json.loads(data.text)
              return tt

          f = r"https://official-joke-api.appspot.com/jokes/programming/random"
          a = jokes(f)

          

          for i in (a):
            await message.channel.send(i["setup"])
            await message.channel.send(i["punchline"])

    if message.content.startswith('$jokes/knock-knock'):
          def jokes(f):
    
              data = requests.get(f)
              tt = json.loads(data.text)
              return tt

          f = r"https://official-joke-api.appspot.com/jokes/knock-knock/random"
          a = jokes(f)

          

          for i in (a):
            await message.channel.send(i["setup"])
            await message.channel.send(i["punchline"])

    if message.content.startswith('$even/odd '):
            a1 = message.content
            e1 = a1.split(' ')
            l1 = list(e1)
            
            l1.pop(0)
            if len(l1) == 0:
              await message.channel.send('Sorry there are not enough numbers in this command')
              return
              
            try:
              for i in range(0, len(l1)):
                  if l1[i] == 'pi':
                    l1[i] = '3.14'  
                  l1[i] = float(l1[i])
            except: 
              await message.channel.send("Sorry your command was not valid. This could have been caused by typing a letter in the numbers or typing the numbers more than 1 space apart")
              return

            for n in range(len(l1)):
              if l1[n-1] % 2 == 0:
                l1[n-1] = 'even'
              else: l1[n-1] = 'odd'
            l4 = ' '.join([str(elem) for elem in l1])

            await message.channel.send(l4)

    if message.content.startswith('$prime '):
              n1 = message.content

              n1 = n1.split(' ')

              n1 = list(n1)

              n1.pop(0)  
                
                
              
              n2 = int(n1[0])
              
              if n2 == 1:
                  await message.chanel.send('Not prime')
              i = 2
              # This will loop from 2 to int(sqrt(x))
              while i*i <= n2:
                    # Check if i divides x without leaving a remainder
                    if n2 % i == 0:
                        # This means that n has a factor in between 2 and sqrt(n)
                        # So it is not a prime number
                        await message.channel.send('Not prime')
                        return
                    i += 1

              await message.channel.send('prime')
              # If we did not find any factor in the above loop,
              # then n is a p

     


            

    if message.content.startswith('$help'):
          await message.channel.send('''
1. $calc - calculates the given expression in PEMDAS order

2. $sqrt - Takes the square root of any number you enter

3. $even/odd - checks if number is even or odd

4. $jokes/general - general jokes

5. $jokes/programming - programming jokes

6. $jokes/knock-knock - Knock-knock jokes

5. $prime - checks if number is prime or not prime. Only works with 1 number at a time. Does not work with decimal numbers.

Thx! for checking this out

NOTE: All numbers must be seperated by spaces except in $calc''')

              
            

            
            
   

      
      

client.run(os.getenv('TOKEN'))
