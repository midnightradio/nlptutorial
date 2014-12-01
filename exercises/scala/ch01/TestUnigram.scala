import scala.math
import scala.collection.mutable.ListBuffer

object TestUnigram extends App {
  val TestInput     = "../../../test/01-test-input.txt"
  val TestDataFile  = "../../../data/wiki-en-test.word"
  val ModelFile     = "./model_file"
  val filename = if (args.length >= 1 && new java.io.File(args(0)).exists) args(0) else TestInput

  val lambda_one  = .95
  val lambda_unk  = 1-lambda_one
  var (v:Int, w:Int, h:Double, unk:Int) = (1000000, 0, .0, 0)

  /*  
  io.Source.fromFile(ModelFile).getLines.toList.foreach {(line:String) =>
    line.split("\t") match {
      case Array(word:String, count:String) => (word, count.toInt)
      case _ => new Exception("Exception")
    }
  }
  */
  def log2(x:Double):Double = math.log(x) / math.log(2)
  val prob_dict = io.Source.fromFile(ModelFile).getLines.map(line => line.split("\t")).map { case Array(word:String, prob:String) => (word, prob.toDouble) }.toMap
  io.Source.fromFile(filename).getLines.toList.foreach {(line:String) =>
    val words = line.split("[ \t]+").to[ListBuffer] += "</s>"
    for (word <- words) {
      w += 1
      var p = lambda_unk / v
      if (prob_dict.contains(word)) {
        p += lambda_one * prob_dict(word)
      } else {
        unk += 1
      }
      
      h -= log2(p) 
    }
  }
  println("entropy = " + h/w)
  println("coverage = " + (w-unk).toDouble/w)
}