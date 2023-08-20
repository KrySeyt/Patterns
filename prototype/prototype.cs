namespace ConsoleApp1;

abstract class Prototype
{
    public abstract Prototype Clone();

    public void Show()
    {
        Console.WriteLine(this.GetType().Name);
    }
}

class ConcretePrototypeA : Prototype
{
    public override ConcretePrototypeA Clone()
    {
        return new ConcretePrototypeA();
    }
}

class ConcretePrototypeB : Prototype
{
    public override ConcretePrototypeB Clone()
    {
        return new ConcretePrototypeB();
    }
}

class Client
{
    private Prototype _prototype;

    public Client(Prototype prototype)
    {
        this._prototype = prototype;
    }

    public Prototype GetProduct()
    {
        return this._prototype.Clone();
    }
}

class TestClass {}

class Program
{
    static void Main()
    {
        ConcretePrototypeA prototype = new();
        Client client = new(prototype);
        Prototype product = client.GetProduct();
        product.Show();
    }
}
