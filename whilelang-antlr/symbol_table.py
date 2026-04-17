class SymbolTable:

    def __init__(self):
        self.scopes = [{}]

    def enter_scope(self):
        self.scopes.append({})
    
    def exit_scope(self):
        self.scopes.pop()

    def declare(self,name, type_):
        scope = self.scopes[-1]
        if name in scopes:
            raise Exception(f"Error: variable '{name}' redeclarada")

    def lookup(self,name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]

        raise Exception(f"Error: variable '{name}' no declarada")
