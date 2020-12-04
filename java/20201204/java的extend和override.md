# java的extend和override

## extend：继承

语法格式：class 子类 extend 父类

公开属性都可以继承

```java
public class abc{
    public static void main (String args[]){
        ...
    }
}
```

public class和class的区别：

1. 带public的class是公共的class，需要和文件名字相同，并且在其他的文件中都可以引用。
2. 当使用class来声明一个类的时候，java编译出来的class文件是和这个类的名字一样的，并且可以用javac来执行。
3. class只有包具有访问权限，其他的包不能访问。
4. Public相当于这个文件对外提供的一个接口，所有有且只能有一个，

java的静态对象能直接调用，但是动态对象需要实例化这个类，才能有一个这个类的实例，再通过这个实例调用其中的函数