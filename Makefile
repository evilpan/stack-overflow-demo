CANARY := -fstack-protector
NO_CANARY := -fno-stack-protector
RELRO := -z relro -z now
NO_RELRO := -z norelro
NX := -z noexecstack
NO_NX := -z execstack
PIE := 
NO_PIE := -no-pie
CFLAGS := -g -m32 -masm=intel 
BINS := victim victim_nx victim_pie

all: $(BINS)

victim : victim.c
	gcc $< -o $@ $(CFLAGS) $(NO_CANARY) $(NO_NX) 

victim_nx : victim.c
	gcc $< -o $@ $(CFLAGS) $(NO_CANARY) $(NX) 

victim_pie: victim.c
	gcc $< -o $@ $(CFLAGS) $(NO_CANARY) $(NX) $(PIE) 

clean:
	rm -rf $(BINS)
