import os

def countRecipes(directory: str):
    recipesCounter = 0

    for directory, subdirectories, files in os.walk(directory):
        recipesCounter += len(files)

    return recipesCounter

def categoryChoice(directory: str):

    print("Estás son las categorías")
    print(os.listdir(directory))

    category = input("Elige una categoría")

    return category, os.path.join(directory, category)

def readRecipe(directory: str):
    category, categoryPath = categoryChoice(directory)

    print(f"Estas son las recetas que se encuentran en la categoría {category}")
    print(os.listdir(categoryPath))

    recipe = input("Elige una receta")
    recipeFile = open(os.path.join(categoryPath, recipe), "r")

    print(recipeFile.read())

def createRecipe(directory: str):
    category, categoryPath = categoryChoice(directory)

    recipeName = input("Nombre de la receta -> ")

    if True == os.path.exists(os.path.join(categoryPath, recipeName)):
        print("La receta ya existe")
        return

    recipeContent = input("Contenido de la receta -> ")

    recipeFile = open(os.path.join(categoryPath, recipeName), "w")
    recipeFile.write(recipeContent)

def createCategory(directory: str):
    categoryName = input("Nombre de la categoria -> ")

    if True == os.path.exists(os.path.join(directory, categoryName)):
        print("La categoría ya existe")
        return

    os.makedirs(os.path.join(directory, categoryName))

def removeRecipe(directory: str):
    category, categoryPath = categoryChoice(directory)

    print(f"Estas son las recetas que se encuentran en la categoría {category}")
    print(os.listdir(categoryPath))

    recipeFile = input("Escoge la receta a eliminar -> ")
    recipePath = os.path.join(categoryPath, recipeFile)

    try:
        os.remove(recipePath)
        print(f"El archivo '{recipePath}' ha sido eliminado exitosamente.")
    except FileNotFoundError:
        print(f"El archivo '{recipePath}' no se encuentra.")
    except Exception as e:
        print(f"Error al eliminar el archivo: {e}")

def removeCategory(directory: str):
    category, categoryPath = categoryChoice(directory)

    try:
        os.removedirs(categoryPath)
        print(f"El directorio '{categoryPath}' ha sido eliminado exitosamente.")
    except FileNotFoundError:
        print(f"El directorio '{categoryPath}' no se encuentra.")
    except Exception as e:
        print(f"Error al eliminar el directorio: {e}")

currentDirectory = os.path.join(os.getcwd(), "Recetas")
totalRecipes = countRecipes(currentDirectory)

def showMenu():
    print("[1] - Leer Receta")
    print("[2] - Crear Receta")
    print("[3] - Crear Categoría")
    print("[4] - Eliminar Receta")
    print("[5] - Eliminar Categoría")
    print("[6] - Finalizar sesión")

print('Bienvenido al recetario\n')
print('Las recetas están en ' + currentDirectory + "\n")
print(f"Tienes {totalRecipes} recetas\n")

choice = 0

while choice != 6:
    showMenu()

    choice = int(input())

    match choice:
        case 1:
            readRecipe(currentDirectory)
        case 2:
            createRecipe(currentDirectory)
        case 3:
            createCategory(currentDirectory)
        case 4:
            removeRecipe(currentDirectory)
        case 5:
            removeCategory(currentDirectory)
        case 6:
            pass
        case _:
            print("Opción no válida")
