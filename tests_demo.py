
from core import QuoteInput, cotizar
def pesos(x): 
    return f"${x:,.0f}"

q1 = cotizar(QuoteInput(2,3,0,"ciudad","C-100","3001234567","cliente1@email.com"))
print("Caso 1 total:", pesos(q1.total_pagar))

q2 = cotizar(QuoteInput(3,2,1,"fuera","C-200","3007654321","cliente2@email.com"))
print("Caso 2 total:", pesos(q2.total_pagar))

q3 = cotizar(QuoteInput(5,1,4,"local","C-300","3009876543","cliente3@email.com"))
print("Caso 3 total:", pesos(q3.total_pagar))

try:
    cotizar(QuoteInput(1,1,0,"ciudad","C-ERR","300123","test@email.com"))
except Exception as e:
    print("Validación OK (equipos):", str(e))

try:
    cotizar(QuoteInput(2,0,0,"ciudad","C-ERR2","300123","test@email.com"))
except Exception as e:
    print("Validación OK (días):", str(e))

try:
    cotizar(QuoteInput(2,1,0,"ciudad","C-ERR3","300123","email-invalido"))
except Exception as e:
    print("Validación OK (email):", str(e))
