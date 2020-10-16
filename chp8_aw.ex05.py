def endswithcom(stringvalue):
    status = stringvalue.endswith(".com")
    return status
value = input(f"please enter an email address:")

answer =endswithcom(value)
print(answer)
