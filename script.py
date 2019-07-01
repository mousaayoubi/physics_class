train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

#Convert 100F to C
f100_in_celsius = f_to_c(100)
print("100 F is "+str(f100_in_celsius)+" C")

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

#Covert 0C to F
c0_in_fahrenheit = c_to_f(0)
print("0 C is "+str(c0_in_fahrenheit)+ " F")

def get_force(mass, acceleration):
  return mass * acceleration

#Print Train Force
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies "+str(train_force)+" Newtons of force.")


#Train work
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does "+str(train_work)+" Joules of work over "+str(train_distance)+" meters.")