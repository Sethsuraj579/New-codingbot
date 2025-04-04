public class timedComputation {
    public static void main(String[] args) {
        long starttime;
        long endtime;
        double time;
        starttime = System.currentTimeMillis();
        double width, height, hypotenus;
        width = 42.0;
        height = 17.0;
        hypotenus = Math.sqrt((width * width) + (height * height));
        System.out.println("The hypotenus is ");
        System.out.println(hypotenus);

        System.out.println("\n Mathematicall, sin(x)*sin(x) + cos(x)*cos(x) - 1 = 0");
        System.out.println("lets check this for x = 1");
        double x = 1;
        System.out.println(
                "sin(x)*sin(x) + cos(x)*cos(x) - 1 = " + (Math.sin(x) * Math.sin(x) + Math.cos(x) * Math.cos(x) - 1));
        System.out.println("There can be a round off error when " + "computing with real numbers");
        System.out.println("Here is the random number generator");
        for (int i = 0; i < 10; i++) {
            System.out.println(Math.random());

            endtime = System.currentTimeMillis();
            time = (endtime - starttime) / 1000.0;
            System.out.println("The time taken to run the program is " + time + " seconds");
        }
    }
}
