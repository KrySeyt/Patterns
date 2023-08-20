#include <iostream>


class Target
{
public:
    virtual void Show() = 0;
};

class Adaptee
{
public:
    std::string GetName()
    {
        return "Adaptee object";
    }
};

class Adapter : public Target, private Adaptee
{
    void Show() override
    {
        std::cout << Adaptee::GetName();
    }
};

int main() {
    Target* targetObject = new Adapter();
    targetObject->Show();
    return 0;
}
