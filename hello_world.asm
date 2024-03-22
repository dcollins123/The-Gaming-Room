section .data
    hello_world db 'Hello, World!', 0

section .text
    global _start

_start:
    ; Write the string to stdout
    mov eax, 4              ; syscall number for sys_write
    mov ebx, 1              ; file descriptor 1 (stdout)
    mov ecx, hello_world    ; pointer to the string
    mov edx, 13             ; length of the string
    int 0x80                ; make the system call

    ; Exit the program
    mov eax, 1              ; syscall number for sys_exit
    xor ebx, ebx            ; exit status 0
    int 0x80                ; make the system call
