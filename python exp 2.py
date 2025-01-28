class Employee:
    def __init__(
            self,
            designation: str = 'Developer',
            frontend: bool = False,
            backend: bool = True
    ):
        self.designation = designation
        self.frontend = frontend
        self.backend = backend

    def __repr__(self):
        return '{} (Frontend: {}, Backend: {})'.format(self.designation, self.frontend, self.backend)

    def verifier(self):
        if self.frontend and self.backend:
            return 'You are a Full Stack Developer'
        elif self.frontend and not self.backend:
            return 'You are a Frontend Developer'
        elif not self.frontend and self.backend:
            return 'You are a Backend Developer'
        else:
            return 'You are a looser'

if __name__ == '__main__':
    firstEmployee = Employee(designation="Full Stack Developer", frontend=True, backend=True)
    print(firstEmployee.verifier())

    secondEmployee = Employee(designation="Backend Developer", frontend=False, backend=True)
    print(secondEmployee.verifier())

    thirdEmployee = Employee(designation="No Developer", frontend=False, backend=False)
    print(thirdEmployee.verifier())