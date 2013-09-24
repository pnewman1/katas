#!/usr/bin/python

#http://community.topcoder.com/stat?c=problem_statement&pm=12300&rd=15699

class JumpFurther:

    def furthest(self, n, BadStep):
        cur_step = 0

        f = lambda b: (b - 1) / 2
    
        if BadStep == 1:
            skip = 1
        else:
            skip = f(BadStep)
    
        for i in range(0, n+1):
            if i == skip:
               pass
            else:
               cur_step+=i

        return cur_step
