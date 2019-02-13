
## 分类
#### 创建型
    抽象工厂
#### 结构性

#### 行为型
    观察者模式


## 原则

solid

#### 单一职责原则(Single Responsibility Principle, SRP)
> 类功能尽量单一，只负责一个功能

#### 里氏替换原则(Liskov Substitution Principle, LSP)

> 所有引用基类的地方，必须能够透明地使用其子类的对象

#### 依赖倒置原则(Dependence Inversion Principle, DIP)

> 高层模块不应该依赖低层模块，二者都应该依赖其抽象
> 抽象不应该依赖细节，细节应该依赖抽象

> 要依赖接口而不是具体实现

#### 接口隔离原则(Interface Segregation Principle, ISP)

> 客户端不应该依赖它不需要的接口
> 一个类对另一个类的依赖应该建立在最小的接口上

> 接口的定义要内聚和单一

#### 迪米特法则(Law of Demeter, LoD)

> 一个对象应该对其他对象保持最少的了解

> 类对外公开的方法和属性要适中

#### 开放封闭原则(Open Close Principle, OCP)

> 对扩展开放，对修改封闭