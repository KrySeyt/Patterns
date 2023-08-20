namespace patterns.abstract_factory;

abstract class Showable
{
    public void Show()
    {
        Console.WriteLine(this.GetType().Name);
    }
}

abstract class FirstProduct : Showable
{
    public abstract FirstProduct Clone();
}

abstract class SecondProduct : Showable
{
    public abstract SecondProduct Clone();
}

abstract class ThirdProduct : Showable
{
    public abstract ThirdProduct Clone();
}

class FirstProductA : FirstProduct
{
    public override FirstProductA Clone()
    {
        return new FirstProductA();
    }
}

class FirstProductB : FirstProduct
{
    public override FirstProductB Clone()
    {
        return new FirstProductB();
    }
}

class SecondProductA : SecondProduct
{
    public override SecondProductA Clone()
    {
        return new SecondProductA();
    }
}

class SecondProductB : SecondProduct
{
    public override SecondProductB Clone()
    {
        return new SecondProductB();
    }
}

class ThirdProductA : ThirdProduct
{
    public override ThirdProductA Clone()
    {
        return new ThirdProductA();
    }
}

class ThirdProductB : ThirdProduct
{
    public override ThirdProductB Clone()
    {
        return new ThirdProductB();
    }
}

class ProductFactory
{
    private FirstProduct _firstProductProto;
    private SecondProduct _secondProductProto;
    private ThirdProduct _thirdProductProto;
    
    public ProductFactory(
        FirstProduct firstProductProto,
        SecondProduct secondProductProto,
        ThirdProduct thirdProdictProto
    )
    {
        _firstProductProto = firstProductProto;
        _secondProductProto = secondProductProto;
        _thirdProductProto = thirdProdictProto;
    }
    
    public FirstProduct CreateFirstProduct()
    {
        return this._firstProductProto.Clone();
    }

    public SecondProduct CreateSecondProduct()
    {
        return this._secondProductProto.Clone();
    }

    public ThirdProduct CreateThirdProduct()
    {
        return this._thirdProductProto.Clone();
    }
}

class Program
{
    static void Main()
    {
        FirstProductA firstProductProto = new();
        SecondProductA secondProductProto = new();
        ThirdProductA thirdProductProto = new();
        ProductFactory productFactory = new(
            firstProductProto,
            secondProductProto,
            thirdProductProto
        );

        FirstProduct firstProduct = productFactory.CreateFirstProduct();
        firstProduct.Show();

        SecondProduct secondProduct = productFactory.CreateSecondProduct();
        secondProduct.Show();

        ThirdProduct thirdProduct = productFactory.CreateThirdProduct();
        thirdProduct.Show();
    }
}