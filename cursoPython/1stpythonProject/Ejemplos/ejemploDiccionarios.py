provincias = dict()

provincias = {
    924: "Badajoz",
    956: "Cádiz",
    958: "Granada",
    959: "Huelva",
    91: "Madrid",
    95: "Málaga",
    968: "Murcia",
    923: "Salamanca",
    95: "Sevilla",
    922: "Sta. Cruz de Tenerife",
    975: "Soria",
    96: "Valencia",
    976: "Zaragoza"
}
print(provincias)

provincias = dict()

provincias = {
    924: "Badajoz",
    956: "Cádiz",
    958: "Granada",
    959: "Huelva",
    91: "Madrid",
    95: "Málaga",
    968: "Murcia",
    923: "Salamanca",
    95: "Sevilla",
    922: "Sta. Cruz de Tenerife",
    975: "Soria",
    96: "Valencia",
    976: "Zaragoza"
}
dato = provincias.get(91)
print(dato)

provincias = dict()

provincias = {
    924: "Badajoz",
    956: "Cádiz",
    958: "Granada",
    959: "Huelva",
    91: "Madrid",
    95: "Málaga",
    968: "Murcia",
    923: "Salamanca",
    95: "Sevilla",
    922: "Sta. Cruz de Tenerife",
    975: "Soria",
    96: "Valencia",
    976: "Zaragoza"
}
for clave, valor in provincias.items():
    print("Prefijo: ", clave, "Provincia: ", valor)

provincias = dict()

provincias = {
    924: "Badajoz",
    956: "Cádiz",
    958: "Granada",
    959: "Huelva",
    91: "Madrid",
    95: "Málaga",
    968: "Murcia",
    923: "Salamanca",
    95: "Sevilla",
    922: "Sta. Cruz de Tenerife",
    975: "Soria",
    96: "Valencia",
    976: "Zaragoza"
}
print("Número de provincias:", len(provincias))

provincias = dict()

provincias = {
    924: "Badajoz",
    956: "Cádiz",
    958: "Granada",
    959: "Huelva",
    91: "Madrid",
    95: "Málaga",
    968: "Murcia",
    923: "Salamanca",
    95: "Sevilla",
    922: "Sta. Cruz de Tenerife",
    975: "Soria",
    96: "Valencia",
    976: "Zaragoza"
}
provincias.setdefault(925, "Toledo")
print(provincias)
# Si la clave existe no lo insertará
provincias.setdefault(91, "Toledo")
print(provincias)
provincias[924] = "Madrid1"
print(provincias)
provincias = dict()

provincias = {
    924: "Badajoz",
    956: "Cádiz",
    958: "Granada",
    959: "Huelva",
    91: "Madrid",
    95: "Málaga",
    968: "Murcia",
    923: "Salamanca",
    95: "Sevilla",
    922: "Sta. Cruz de Tenerife",
    975: "Soria",
    96: "Valencia",
    976: "Zaragoza"
}
provincias.clear()
print(provincias)
provincias = dict()

provincias = {
    924: "Badajoz",
    956: "Cádiz",
    958: "Granada",
    959: "Huelva",
    91: "Madrid",
    95: "Málaga",
    968: "Murcia",
    923: "Salamanca",
    95: "Sevilla",
    922: "Sta. Cruz de Tenerife",
    975: "Soria",
    96: "Valencia",
    976: "Zaragoza"
}
provincias.pop(924)
print(provincias)

