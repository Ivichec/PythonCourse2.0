def calcularIVA():
    importe = int(input("Precio del producto: "))
    total = importe * 1.21
    #print("IVA incluido (21%):"+str(total))
    print(f"IVA incluido (21%): {total}")

    return


print("LLAMANDO A LA FUNCIÓN")
calcularIVA()


def calcularIVA(importe):
    print(f"Precio del producto: {importe}")
    total = importe * 1.21
    print(f"IVA incluido (21%): {total}")
    return


print("LLAMANDO A LA FUNCIÓN")
calcularIVA(600)


def calcularIVA(importe):
    print(f"Precio del producto: {importe}")
    total = importe * 1.21
    return total


print("LLAMANDO A LA FUNCIÓN")
result = calcularIVA(1000)
print(f"IVA incluido (21%): {result}")


def calcularIVA(importe):
    total = importe * 1.21
    return importe, total


print("LLAMANDO A LA FUNCIÓN")
precio, result = calcularIVA(2000)

print(f"Precio del producto: {precio}")
print(f"IVA incluido (21%): {result}") 