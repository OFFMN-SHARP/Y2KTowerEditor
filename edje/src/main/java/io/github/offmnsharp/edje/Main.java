package io.github.offmnsharp.edje;

import java.io.File;

public class Main {
    public static void main(String[] args){
        if(args.length==0){//no args
            System.out.print("Message:Mode selected [W]");
            System.out.println();
            EditorW.Write();
            System.exit(0);
        } else if (args.length==1) {//args=1
            if(args[0].equals("/help")){
                return;
            }
            File ModeEx =new File(args[0]);
            if (ModeEx.exists()){
                System.out.print("Message:Mode selected [RW]");
                EditorRW ERW =new EditorRW();
                return;
            }
            System.exit(0);
        } else if (args.length == 2) {//args>1
            File ModeEx =new File(args[0]);
            if(ModeEx.exists()&&args[1].equals("/type")){
                System.out.print("Message:Console output Mode[Type]");
                System.exit(0);
            } else if (ModeEx.exists()&&args[1].equals("/typewriter")) {
                System.out.print("Message:Console output Mode[Typewriter]");
                System.exit(0);
            }
            else {
                System.exit(0);
            }
        }
        else {
            System.exit(0);
        }
    }
}
