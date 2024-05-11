### Lambdas ###

#Son como funciones, pero las Lambdas son funciones anonimas, es decir no tienen nombre

#Las lambda se pueden iniciar dentro de una variable.
sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 4))

multiply_values = lambda  first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))

#Se pueden utilizar una lambda dentro de una función normal
def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))
