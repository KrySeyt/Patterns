namespace ParametrizedAbstractFactory;

abstract class Showable
{
    public void Show()
    {
        Console.WriteLine(this.GetType().Name);
    }
}

abstract class FirstProduct : Showable {}
abstract class SecondProduct : Showable {}
abstract class ThirdProduct : Showable {}

class FirstProductA : FirstProduct {}

class FirstProductB : FirstProduct {}

class SecondProductA : SecondProduct {}
class SecondProductB : SecondProduct {}

class ThirdProductA : ThirdProduct {}
class ThirdProductB : ThirdProduct {}

class ParametrizedProductFactory
{
    public FirstProduct CreateFirstProduct<T>() where T : FirstProduct, new()
    {
        return new T();
    }

    public SecondProduct CreateSecondProduct<T>() where T : SecondProduct, new()
    {
        return new T();
    }

    public ThirdProduct CreateThirdProduct<T>() where T : ThirdProduct, new()
    {
        return new T();
    }
}


class Program
{
    static void Main()
    {
        ParametrizedProductFactory factory = new();
        
        FirstProduct firstProduct = factory.CreateFirstProduct<FirstProductB>();
        firstProduct.Show();
        
        SecondProduct secondProduct = factory.CreateSecondProduct<SecondProductB>();
        secondProduct.Show();
        
        ThirdProduct thirdProduct = factory.CreateThirdProduct<ThirdProductA>();
        thirdProduct.Show();
    }
}