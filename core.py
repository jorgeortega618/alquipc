
from dataclasses import dataclass, asdict
from typing import Literal, Dict
import re

BASE_PRICE = 35000
Location = Literal["ciudad", "fuera", "local"]

@dataclass
class QuoteInput:
    n_equipos: int
    dias_iniciales: int
    dias_adicionales: int
    ubicacion: Location  
    id_cliente: str
    telefono_cliente: str
    email_cliente: str

@dataclass
class QuoteOutput:
    id_cliente: str
    telefono_cliente: str
    email_cliente: str
    n_equipos: int
    dias_iniciales: int
    dias_adicionales: int
    ubicacion: Location
    precio_base_diario: int
    total_inicial: int
    total_adicional: int
    ajuste_ubicacion_pct: float
    ajuste_ubicacion_valor: int
    subtotal: int
    total_pagar: int
    descuentos_aplicados: Dict[str, str]
    incrementos_aplicados: Dict[str, str]

class ValidationError(Exception):
    pass

def _round_pesos(x: float) -> int:
    return int(round(x))

def _ubicacion_factor(ubicacion: Location) -> float:
    if ubicacion == "ciudad":
        return 0.0
    if ubicacion == "fuera":
        return 0.05
    if ubicacion == "local":
        return -0.05
    raise ValidationError("Ubicación no válida")

def validar(entrada: QuoteInput) -> None:
    if entrada.n_equipos < 2:
        raise ValidationError("El número mínimo de equipos es 2.")
    if entrada.dias_iniciales <= 0:
        raise ValidationError("Los días iniciales deben ser un entero positivo.")
    if entrada.dias_adicionales < 0:
        raise ValidationError("Los días adicionales no pueden ser negativos.")
    if entrada.ubicacion not in ("ciudad", "fuera", "local"):
        raise ValidationError("Ubicación debe ser: 'ciudad', 'fuera' o 'local'.")
    if not entrada.id_cliente.strip():
        raise ValidationError("El Id-cliente no puede estar vacío.")
    if not entrada.telefono_cliente.strip():
        raise ValidationError("El teléfono del cliente no puede estar vacío.")
    if not entrada.email_cliente.strip():
        raise ValidationError("El email del cliente no puede estar vacío.")
    
    # Validar formato de email básico
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, entrada.email_cliente):
        raise ValidationError("El formato del email no es válido.")
    
    # Validar teléfono (solo números, espacios, guiones y paréntesis)
    telefono_pattern = r'^[\d\s\-\(\)\+]+$'
    if not re.match(telefono_pattern, entrada.telefono_cliente):
        raise ValidationError("El teléfono solo puede contener números, espacios, guiones y paréntesis.")

def cotizar(entrada: QuoteInput) -> QuoteOutput:
    validar(entrada)
    # Costos
    total_inicial = entrada.n_equipos * entrada.dias_iniciales * BASE_PRICE
    tarifa_extra = BASE_PRICE * (1 - 0.02)
    total_adicional = entrada.n_equipos * entrada.dias_adicionales * tarifa_extra
    subtotal = total_inicial + total_adicional

    # Ajuste de ubicación
    adj = _ubicacion_factor(entrada.ubicacion)
    ajuste_valor = _round_pesos(subtotal * adj)
    total = _round_pesos(subtotal + ajuste_valor)

    descuentos = {}
    incrementos = {}
    if entrada.dias_adicionales > 0:
        descuentos["adicional"] = "2% de descuento por cada día adicional"
    if entrada.ubicacion == "local":
        descuentos["ubicacion"] = "5% de descuento por uso dentro del establecimiento"
    if entrada.ubicacion == "fuera":
        incrementos["ubicacion"] = "5% de recargo por servicio a domicilio (fuera de la ciudad)"

    return QuoteOutput(
        id_cliente=entrada.id_cliente,
        telefono_cliente=entrada.telefono_cliente,
        email_cliente=entrada.email_cliente,
        n_equipos=entrada.n_equipos,
        dias_iniciales=entrada.dias_iniciales,
        dias_adicionales=entrada.dias_adicionales,
        ubicacion=entrada.ubicacion,
        precio_base_diario=BASE_PRICE,
        total_inicial=int(total_inicial),
        total_adicional=_round_pesos(total_adicional),
        ajuste_ubicacion_pct=adj,
        ajuste_ubicacion_valor=ajuste_valor,
        subtotal=_round_pesos(subtotal),
        total_pagar=total,
        descuentos_aplicados=descuentos,
        incrementos_aplicados=incrementos,
    )

def formato_resumen(q: QuoteOutput) -> str:
    ubic = {"ciudad":"Dentro de la ciudad", "fuera":"Fuera de la ciudad", "local":"Dentro del establecimiento"}[q.ubicacion]
    partes = [
        f"ALQUIPC - Resumen de alquiler (Id-cliente: {q.id_cliente})",
        f"Cliente: {q.id_cliente}",
        f"Teléfono: {q.telefono_cliente}",
        f"Email: {q.email_cliente}",
        f"Equipos alquilados: {q.n_equipos}",
        f"Días iniciales: {q.dias_iniciales}",
        f"Días adicionales: {q.dias_adicionales}",
        f"Ubicación del servicio: {ubic}",
        f"Tarifa base diaria por equipo: ${q.precio_base_diario:,.0f} COP",
        f"Subtotal días iniciales: ${q.total_inicial:,.0f}",
        f"Subtotal días adicionales (con 2% desc/ día): ${q.total_adicional:,.0f}",
        f"Subtotal antes de ubicación: ${q.subtotal:,.0f}",
    ]
    if q.ajuste_ubicacion_pct != 0:
        signo = "+" if q.ajuste_ubicacion_pct > 0 else "-"
        partes.append(f"Ajuste por ubicación ({int(abs(q.ajuste_ubicacion_pct)*100)}%): {signo}${abs(q.ajuste_ubicacion_valor):,.0f}")
    if q.descuentos_aplicados:
        desc = "; ".join(q.descuentos_aplicados.values())
        partes.append(f"Descuentos aplicados: {desc}")
    if q.incrementos_aplicados:
        inc = "; ".join(q.incrementos_aplicados.values())
        partes.append(f"Incrementos aplicados: {inc}")
    partes.append(f"TOTAL A PAGAR: ${q.total_pagar:,.0f} COP")
    return "\n".join(partes)

def to_dict(q: QuoteOutput):
    d = asdict(q)
    return d
