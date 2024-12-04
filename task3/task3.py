# https://www.cs.sjsu.edu/~pearce/modules/lectures/prolog/kbase.htm
# https://www.swi-prolog.org/pldoc/man?section=quickstart
# https://www.cs.sjsu.edu/~pearce/modules/lectures/prolog/kbase.htm
# https://pyswip.readthedocs.io/en/stable/api/prolog.html
# https://pypi.org/project/pyswip/
# https://pypi.org/project/pyswip/
# https://pypi.org/project/pyswip/
# https://g.co/gemini/share/dc8720bfffa4
# https://g.co/gemini/share/f0220ed1a8cb
# https://g.co/gemini/share/e6bc3b948180
# https://g.co/gemini/share/8179656a121a
# https://github.com/dsapandora/pyswip/blob/master/pyswip/prolog.py

# Prolog

from pyswip import Prolog

prolog = Prolog()

prolog.assertz('engineer(billy)')
prolog.assertz('engineer(joseph)')
prolog.assertz('engineer(sandra)')
prolog.assertz('engineer(mary)')
prolog.assertz('engineer(tim)')

prolog.assertz('works_on_software(billy)')
prolog.assertz('works_on_software(mary)')
prolog.assertz('works_on_software(tim)')

prolog.assertz('works_on_hardware(joseph)')
prolog.assertz('works_on_hardware(sandra)')

prolog.assertz('software_engineer(X) :- engineer(X), works_on_software(X)')
prolog.assertz('hardware_engineer(X) :- engineer(X), works_on_hardware(X)')

# def query_bool(query_str):
#     query = prolog.query(query_str)
#     result = next(query, None)
#     query.close()
#     return bool(result)

for soln in prolog.query('software_engineer(X).'):
    print('X =', soln['X'])

print()

for soln in prolog.query('hardware_engineer(X).'):
    print('X =', soln['X'])

print()

print(bool(list(prolog.query('software_engineer(billy).'))))
# query = prolog.query('software_engineer(billy).')
# if bool(next(query, None)):
#     print("true")
# else:
#     print("false")
# query.close()
# print(query_bool('software_engineer(billy).'))

print()

print(bool(list(prolog.query('software_engineer(joseph).'))))
# query = prolog.query('software_engineer(joseph).')
# if bool(next(query, None)):
#     print("true")
# else:
#     print("false")
# query.close()
# print(query_bool('software_engineer(joseph).'))

print()