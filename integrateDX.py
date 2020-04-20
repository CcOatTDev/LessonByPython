import sympy as sp 

x= sp.Symbol('x')

problem = '2*x**4+1'
result = str(sp.integrate(2*(x**4)+1,x))

def pownumber(rs):
    
    resulttext = ['','']

    for i in rs:
        if resulttext[-2] == '*' and resulttext[-1] == '*' and i == '2':
            resulttext.append('²')
        elif resulttext[-2] == '*' and resulttext[-1] == '*' and i == '3':
            resulttext.append('³')
        elif resulttext[-2] == '*' and resulttext[-1] == '*' and i == '4':
            resulttext.append('⁴')
        elif resulttext[-2] == '*' and resulttext[-1] == '*' and i == '5':
            resulttext.append('⁵')
        elif resulttext[-2] == '*' and resulttext[-1] == '*' and i == '6':
            resulttext.append('⁶')
        elif resulttext[-2] == '*' and resulttext[-1] == '*' and i == '7':
            resulttext.append('⁷')
        elif resulttext[-2] == '*' and resulttext[-1] == '*' and i == '8':
            resulttext.append('⁸')
        elif resulttext[-2] == '*' and resulttext[-1] == '*' and i == '9':
            resulttext.append('⁹')
        else:
            resulttext.append(i)
    resulttext.remove('')
    resulttext.remove('')

    finaltext = ''

    for j in resulttext:
        if j != '*':
            finaltext += j
        else:
            finaltext = finaltext

    return finaltext

textpb = pownumber(problem)
textres = pownumber(result)

print("∫ {} dx = {}".format(textpb,textres))
