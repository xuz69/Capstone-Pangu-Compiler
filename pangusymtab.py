# pangusymtab.py
# Symbol Table
import sys

# Symbol class
class Symbol:
    # id,scope,kind,type,signature,pline,ppos
    def __init__(self,id=None,scope=None,kind=None,type=None,signature=None,pline=None,ppos=None):
        if id == None and scope == None and kind == None:
            print("Symbol __init__ error: id, scope, and kind must be specified")
            sys.exit(0)
        # length >= 3
        self.name = id # name of the variable
        self.scope = scope # scope of the variable; e.g. global, local, class A etc.
        self.kind = kind # e.g. attribute, global, local variable
        self.type = type # type of the variable; e.g. int, boolean etc.
        self.signature = signature # signature is not None if it is a method or constr
        self.pline = pline # line where the variable 
        self.ppos = ppos # position on that line
    #end __init__

    def d_name(self):
        return self.name

    def d_scope(self):
        return self.scope

    def d_kind(self):
        return self.kind

# SymbolTab class
class SymbolTab:
    def __init__(self,*argv):
        self.table = [] # list of Symbol Object
    
    # insert symbol into the table
    def insertSymbol(self,id=None,scope=None,kind=None,type=None,signature=None,pline=None,ppos=None):
        s = Symbol(id=id,scope=scope,kind=kind,type=type,signature=signature,pline=pline,ppos=ppos)
        self.table.append(s)

    # print out the symbol table
    def showtab(self):
        for i in self.table:
            print("--------------------------------------------\n")
            print(i.name,": ",end="")
            print("scope = ",i.scope," | ",end="")
            print("kind = ",i.kind," | ",end="")
            if i.type:
                print("type = ",i.type," | ",end="")
            if i.signature:
                print("signature = ",i.signature," | ",end="")
            if i.pline:
                print("pline = ",i.pline," | ",end="")
            if i.ppos:
                print("ppos = ",i.ppos," | ",end="")
            print("\n")     

    # check whether it is a defined classname
    def is_classname(self,xid):
        for i in self.table:
            if xid == i.name:
                if i.scope == "global":
                    if i.kind == "classname":
                        return i
        return None
    
    # check whether it is a defined constr method name in the same scope
    def is_constr(self,xid,scope,signature):
        for i in self.table:
            if xid == i.name:
                if i.scope == scope:
                    if i.kind == "constr":
                        if i.signature == signature:
                            return i
        return None

    # check whether it is a defined method with same signature in the same scope
    def is_method(self,xid,scope,signature):
        for i in self.table:
            if i.name == xid:
                if i.scope == scope:
                    if i.kind == "method":
                        if i.signature == signature:
                            return i
        return None
    
    # check whether it is a defined method name with the same scope
    def is_methodname(self,xid,scope):
        for i in self.table:
            if i.name == xid:
                if i.scope == scope:
                    if i.kind == "method":
                        return i
        return None
    
    # check whether it is a defined attribute name with the same scope
    def is_attribute(self,name,scope):
        for i in self.table:
            if i.name == name:
                if i.scope == scope:
                    if i.kind == "attribute":
                        return i
        return None 

    # check whether it is a defined variable with the same scope
    def is_var(self,varname,scope):
        for i in self.table:
            if i.name == varname:
                if i.scope == scope:
                    if i.kind == "var":
                        return i
        return None
    
    # check whether it is a defined label with the same scope
    def is_label(self,labelname,scope):
        for i in self.table:
            if i.name == labelname:
                if i.scope == scope:
                    if i.kind == "label":
                        return i
        return None
    
    # check whether it is a defined argument with the same scope
    def is_arg(self,varname,scope):
        for i in self.table:
            if i.name == varname:
                if i.scope == scope:
                    if i.kind == "arg":
                        return i
        return None
    
    # find the Symbol Object based on the given name and scope
    def find(self,name,scope):
        for i in self.table:
            if i.name == name:
                if i.scope == scope:
                    print("is defined in ", i.scope,"and the type is ",i.type)
                    return i
        return None
