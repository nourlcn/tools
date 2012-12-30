package tools

imoprt "math"

func IsEqual(f1,f2,p float64){
	return math.Abs(f1-f2) < p
}
