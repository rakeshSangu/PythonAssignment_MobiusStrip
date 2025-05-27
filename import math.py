import math

class MobiusStrip:
    def __init__(self,R,w,n):
        self.R = R #radius
        self.w = w #width
        self.n = n #points size
        self.u_values = []
        self.v_values = []
        for i in range(n+1):
            self.u_values.append(2*math.pi*i/n)
            self.v_values.append((-w/2) + w*i/n)
        self.points = self.generate_points_mesh()
    
    def parametric_equation(self,u,v):
        #using given parametric_equations
        x = (self.R + v*math.cos(u/2))*math.cos(u)
        y = (self.R + v*math.cos(u/2))*math.sin(u)
        z = v*math.sin(u/2)
        return (x,y,z)
    
    def generate_points_mesh(self):
        points_list = []
        for u in self.u_values:
            row = []
            for v in self.v_values:
                row.append(self.parametric_equation(u,v))
            points_list.append(row)
        
        return points_list
    
    def distance(self,p1,p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        dz = p2[2] - p1[2]
        return math.sqrt(dx**2 + dy**2 + dz**2)
    
    
    def edge_length(self):
        length = 0
        for i in range(self.n):
            p1 = self.points[0][i]
            p2 = self.points[0][i+1]
            length += self.distance(p1,p2) #for u=0
        
        for i in range(self.n):
            p1 = self.points[-1][i]
            p2 = self.points[-1][i+1]
            length += self.distance(p1,p2) #for u=2pi
        
        return length
    
    def triangle_area(self,p1,p2,p3):
        #using cross product
        ax,ay,az = p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2]
        bx,by,bz = p3[0]-p1[0], p3[1]-p1[1], p3[2]-p1[2]
        cx = ay*bz - az*by 
        cy = az*bx - ax*bz
        cz = ax*by - ay*bx 
        area = 0.5*math.sqrt(cx**2 + cy**2 +cz**2) #area of triangle formula
        return area
        
    
    def surface_area(self):
        area = 0 
        #considering as a square formed by 4 points, we are finding area of 2 triangles,whose sum is equal to square area 
        for i in range(self.n):
            for j in range(self.n):
                p1 = self.points[i][j]
                p2 = self.points[i+1][j]
                p3 = self.points[i][j+1]
                p4 = self.points[i+1][j+1]

                area += self.triangle_area(p1,p2,p3) #triangle_area_1
                area += self.triangle_area(p2,p4,p3) #triangle_area_2
        return area
        
        
mesh = MobiusStrip(5,2,100) #sample calculation
print(mesh.edge_length())
print(mesh.surface_area())