import argparse, sys, json
from core import QuoteInput, cotizar, formato_resumen, to_dict

def main():
    p = argparse.ArgumentParser(description="ALQUIPC - Facturación de alquiler de portátiles")
    p.add_argument("--id", dest="id_cliente", required=True, help="Id del cliente asignado")
    p.add_argument("--telefono", dest="telefono_cliente", required=True, help="Teléfono del cliente")
    p.add_argument("--email", dest="email_cliente", required=True, help="Email del cliente")
    p.add_argument("--equipos", type=int, required=True, help="Número de equipos (mínimo 2)")
    p.add_argument("--dias", type=int, required=True, help="Días iniciales de alquiler (>=1)")
    p.add_argument("--extra", type=int, default=0, help="Días adicionales (>=0)")
    p.add_argument("--ubicacion", choices=["ciudad","fuera","local"], required=True,
                   help="Lugar del servicio: ciudad | fuera | local")
    p.add_argument("--json", action="store_true", help="Imprime salida en JSON además del resumen humano")
    args = p.parse_args()

    try:
        q = cotizar(QuoteInput(
            n_equipos=args.equipos,
            dias_iniciales=args.dias,
            dias_adicionales=args.extra,
            ubicacion=args.ubicacion,
            id_cliente=args.id_cliente,
            telefono_cliente=args.telefono_cliente,
            email_cliente=args.email_cliente
        ))
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    print(formato_resumen(q))
    if args.json:
        print("\nJSON:", json.dumps(to_dict(q), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
