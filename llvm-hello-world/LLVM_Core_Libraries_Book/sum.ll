; ModuleID = 'sum.bc'
source_filename = "sum.ll"
target triple = "x86_64-apple-macosx12.0.0"

define private i32 @sum(i32 %a, i32 %b) {
entry:
  %a.addr = alloca i32, align 4
  %b.addr = alloca i32, align 4
  store i32 %a, i32* %a.addr, align 4
  store i32 %b, i32* %b.addr, align 4
  %0 = load i32, i32* %a.addr, align 4
  %1 = load i32, i32* %b.addr, align 4
  %add = add i32 %0, %1
  ret i32 %add
}
