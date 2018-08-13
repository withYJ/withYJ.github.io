# Python Object-Oriented Programming

### 절차지향 프로그래밍  VS  객체지향 프로그래밍

절차지향 프로그래밍은

- "함수의 집합"으로 실세계의 문제를 풀어간다.

  → Top-Down 방식으로 함수를 디자인한다.

- 데이터와 함수를 분리해서 다룬다.



객체지향 프로그래밍은

- "클래스의 집합"으로 실세계의 문제를 풀어간다.

- 데이터와 함수를 모아서 캡슐화 시킨 클래스를 만들어 다룬다.

  → 클래스란 사용자가 정의한 추상화된 데이터 타입이다.

  → 이로인해 필요한 기능별로 묶어서 모듈화하여 프로그래밍 개발할 수 있다.

- 또한, 클래스를 이어 받아서 새로운 클래스를 생성하는 "상속"도 가능하다.

  → 이는 코드 재사용 및 간결하고 직관적인 코딩을 하는데 큰 도움이 된다.



> Class에 정의된 변수는 variable, instance variable, structural part, attribute, property, representaion 으로
>
> 함수는 function, procedure, action, operation, method, instance method, behavior 로 지칭한다.





### Python OOP Tutorial

1. 클래스 작성 방법

```python
class BaseClass:	# 1) class 라는 reserved word로 시작한다. 2) class 이름은 PascalCase 로 작성.
    def printHam(self):    # 3) class 내에서 정의된 함수 인스턴스는 ()안에 첫 단어는 self를 적는다.
        """        
        self 자체에 의미가 있는 것은 아니고(다른 문자 입력해도 동작은 동일함), 함수의 첫번째 파라미터로 
        class 자신의 주소를 자동으로 넘겨준다.
        (예시와 함께 더 깊게 이해하려면 https://wikidocs.net/1742 참고하면 좋겠다.)
        """        				 
        print 'ham'
        
class InheritingClass(BaseClass):    # 4) 상속하려면 괄호안에 부모 class를 적어주면 된다.
    pass
```



2. 





일반적인 사용 예시를 살펴보자.

```python
# Instance Variable vs Class Variable, Instance Method vs Class Method
# Special variable : __dict__, __doc__, __name__, __module__, __bases__,
# hasattr(Obj, 'attributeName'), getattr(Obj, 'attributeName'),
# setattr(Obj, 'attributeName', 'attributeValue'), delattr(Obj, 'attributeName')
# __init__() + 상속 막는 방법, __del__(), __add__(), __sub__(), __mult()__, __div__(), __float__(), __str__(), __repr__(), __hash__(), __lt__(), __le__(), __gt__(), __ge__(), __eq__(), __iter__(), __next__()
# 상속 규칙
```



https://repl.it/@youngjoonLee/ArtisticAwfulAssemblylanguage



<iframe height="400px" width="100%" src="https://repl.it/@youngjoonLee/ArtisticAwfulAssemblylanguage?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>













