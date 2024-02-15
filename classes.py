class Forex:
    def yenToUSD(yen):
        usd = yen * 0.0067
        print(f"¥{yen:,} -> ${round(usd, 2):,}")

    def usdToYEN(usd):
        yen = usd / 0.0067
        print(f"${usd:,} -> ¥{round(yen, 2):,}")


class Temp:
    def CtoF(C):
        F = (C * (9 / 5)) + 32
        return print(f"{C}°C -> {round(F, 2)}°F")


# Forex.yenToUSD(float(input("Enter Amount: ¥")))
# Forex.usdToYEN(float(input("Enter Amount: $")))
Temp.CtoF(int(input("Enter Celsius: ")))
