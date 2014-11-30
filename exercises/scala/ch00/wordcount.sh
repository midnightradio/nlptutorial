#!/bin/sh
exec scala "$0" "$@"
!#

import scala.collection.mutable.Map

object WordCount extends App {
  val TestInput  = "../../../test/00-input.txt"
  val TestAnswer = "../../../test/00-answer.txt"
  val DataFile   = "../../../data/wiki-en-train.word"

  def report(counter:Map[String, Int]):Unit = {
    for ((w,c) <- counter) {
      println(w + "\t" + c)
    }
    
    println(counter.filter { case (w:String, c:Int) => c == 1 }.map(_ => 1).sum)
    val result = List("in", "on", "with", "to", "the", "a")
    println(result.map(word => counter(word)).mkString(" "))
    
  }
  
  def wordcount(filename:String): Map[String,Int] = {
    val counter = Map[String, Int]().withDefaultValue(0)
    try {
        io.Source.fromFile(filename).getLines.toList.foreach {(line:String) =>
          for (word <- line.split("[ \t]+")) {
              counter.update(word, counter(word) + 1)
          }
        }
    } catch {
        case e:Exception => println("Exception")
    }
    counter
  }
  
  val filename:String = if (args.length >= 1 && new java.io.File(args(0)).exists) args(0) else DataFile
  val counter = wordcount(filename)
  report(counter)
}

WordCount.main(args)
