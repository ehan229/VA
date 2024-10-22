#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int getAge();
		void setAge(int);
		int getDecades();
		int fib(int); //
	private:
		int age;
	};
 
Person::Person(int a){
	age = a;
	}
 
int Person::getAge(){
	return age;
	}
 
void Person::setAge(int a){
	age = a;
	}

int Person::getDecades(){
	return age/10;
	}
// fib
int Person::fib(int n){
    if (n <= 1)
        return n;
    else
            return fib(n-1) + fib(n-2);
    }

extern "C"{
	Person* Person_new(int a) {return new Person(a);}
	int Person_getAge(Person* person) {return person->getAge();}
	void Person_setAge(Person* person, int a) {person->setAge(a);}
	int Person_getDecades(Person* person) {return person->getDecades();}
	long long Person_fib(Person* person, int n) {if (n<=1) {return n; }return Person_fib(person,n-1)+Person_fib(person,n-2);}  //add fib
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}