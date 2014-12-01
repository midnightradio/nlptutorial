import scala.collection.mutable.{Map, ListBuffer}
import scala.collection.immutable.TreeMap

object TrainUnigram extends App {
  val counter = Map[String, Int]().withDefaultValue(0)
  
  val TrainInput     = "../../../test/01-train-input.txt"
  val TrainDataFile  = "../../../data/wiki-en-train.word"
  val ModelFile     = "./model_file"
  val filename = if (args.length >= 1 && new java.io.File(args(0)).exists) args(0) else TrainInput
  
  io.Source.fromFile(filename).getLines.toList.foreach {(line:String) =>
    val words = line.split("[ \t]+").to[ListBuffer] += "</s>"
    for (word <- words) {
      counter.update(word, counter(word) + 1)
    }
  }
  val total_count = counter.valuesIterator.sum
  // http://stackoverflow.com/a/3074156/1542390
  
  try {
    val outs = new java.io.PrintStream(new java.io.File(ModelFile))
      
    TreeMap(counter.toArray:_*).foreach { case (word:String, count:Int) =>
      Console.withOut(outs) { println(word + "\t" + count) }
    }
  } catch {
    case e:Exception => println("Exception")
  }
}