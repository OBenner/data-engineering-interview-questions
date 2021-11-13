[Interview questions](full.md)
# Apache Avro
+ [What is Apache Avro?](#What-is-Apache-Avro)
+ [State some Key Points about Apache Avro?](#State-some-Key-Points-about-Apache-Avro)
+ [What Avro Offers?](#What-Avro-Offers)
+ [Who is intended audience to Learn Avro?](#Who-is-intended-audience-to-Learn-Avro)
+ [What are prerequisites to learn Avro?](#What-are-prerequisites-to-learn-Avro)
+ [Explain Avro schemas?](#Explain-Avro-schemas)
+ [Explain Thrift and Protocol Buffers and Avro?](#Explain-Thrift-and-Protocol-Buffers-and-Avro)
+ [Why Avro?](#Why-Avro)
+ [How to use Avro?](#How-to-use-Avro)
+ [Name some primitive types of Data Types which Avro Supports.](#Name-some-primitive-types-of-Data-Types-which-Avro-Supports)
+ [Name some complex types of Data Types which Avro Supports.](#Name-some-complex-types-of-Data-Types-which-Avro-Supports)
+ [What are best features of Apache Avro?](#What-are-best-features-of-Apache-Avro)
+ [Explain some advantages of Avro.](#Explain-some-advantages-of-Avro)
+ [Explain some disadvantages of Avro.](#Explain-some-disadvantages-of-Avro)
+ [What do you mean by schema declaration?](#What-do-you-mean-by-schema-declaration)
+ [Explain the term Serialization?](#Explain-the-term-Serialization)
+ [What do you mean by Schema Resolution?](#What-do-you-mean-by-Schema-Resolution)
+ [Explain the Avro Sasl profile?](#Explain-the-Avro-Sasl-profile)
+ [What is the way of creating Avro Schemas?](#What-is-the-way-of-creating-Avro-Schemas)
+ [Name some Avro Reference Apis?](#Name-some-Avro-Reference-Apis)
+ [When to use Avro?](#When-to-use-Avro)
+ [Explain sort order in brief?](#Explain-sort-order-in-brief)
+ [What is the advantage of Hadoop Over Java Serialization?](#What-is-the-advantage-of-Hadoop-Over-Java-Serialization)
+ [What are the disadvantages of Hadoop Serialization?](#What-are-the-disadvantages-of-Hadoop-Serialization)

## What is Apache Avro?
An open source project which offers data serialization as well as data exchange services for Apache Hadoop is what we call Apache Avro. It is possible to use these services together or independently both. However, programs can efficiently serialize data into files or into messages, with the serialization service. In addition, data storage is very compact and efficient in Avo because here data definition is in JSON, so, data itself is stored in the binary format making it compact and efficient.

[Table of Contents](#Apache-Avro)

## State some Key Points about Apache Avro?
Some key points are:
+ Avro is a Data serialization system
+ It uses JSON based schemas
+ Moreover, to send data, it uses RPC calls.
+ And, during data exchange, Schema’s sent.

[Table of Contents](#Apache-Avro)

## What Avro Offers?
Avro offers:
+ Avro offers Rich data structures.
+ And, a compact, fast, binary data format.
+ Further, it offers a container file, to store persistent data.
+ Remote procedure calls (RPC).

[Table of Contents](#Apache-Avro)

## Who is intended audience to Learn Avro?
Those people who want to learn the basics of Big Data Analytics by using Hadoop Framework and also those who aspire to become a successful Hadoop developer can go for Avro. Further, those aspirants who want to use Avro for data serialization and deserialization can also learn Avro.

[Table of Contents](#Apache-Avro)

## What are prerequisites to learn Avro?
Those who want to learn Avro must know Hadoop’s architecture and APIs, before learning Avro. Also, must know Java with experience in writing basic applications before going for Avro.

[Table of Contents](#Apache-Avro)

## Explain Avro schemas?
Mainly, Avro heavily depends on its schema. Basically, it permits every data to be written with no prior knowledge of the schema. We can say Avro serialized fast and the data resulting after serialization is least in size with schemas.

[Table of Contents](#Apache-Avro)

## Explain Thrift and Protocol Buffers and Avro?
The most competent libraries with Avro are Thrift and Protocol Buffers.
The difference between them is: − As per the need, Avro supports both dynamic and static types. Basically, to specify schemas and their types, Protocol Buffers and Thrift uses Interface Definition Languages (IDLs).
As Avro is built in the Hadoop ecosystem but Thrift and Protocol Buffers are not.

[Table of Contents](#Apache-Avro)

## Why Avro?
Some features where Avro differs from other systems are:
+ Dynamic typing.
+ Untagged data.
+ No manually-assigned field IDs.

[Table of Contents](#Apache-Avro)

## How to use Avro?
The workflow to use Avro is:− We need to create schemas at first to read the schemas into our program that is possible in two ways.
Generating a Class Corresponding to Schema Using Parsers Library
Then perform the serialization by using serialization API provided for Avro. And then perform deserialization by using deserialization API provided for Avro.

[Table of Contents](#Apache-Avro)

## Name some primitive types of Data Types which Avro Supports.
Avro supports a wide range of Primitive datatypes:
+ Null: no value
+ Boolean: a binary value
+ Int: 32-bit signed integer
+ Long: 64-bit signed integer
+ Float: single precision (32-bit) IEEE 754 floating-point number
+ Double: double precision (64-bit) IEEE 754 floating-point number
+ Bytes: the sequence of 8-bit unsigned bytes
+ String: Unicode character sequence

[Table of Contents](#Apache-Avro)

## Name some complex types of Data Types which Avro Supports.
There are six kinds of complex types which Avro supports:
+ Records
+ Enums
+ Arrays
+ Maps
+ Unions
+ Fixed

[Table of Contents](#Apache-Avro)

## What are best features of Apache Avro?
Some of the best features of Avro are:
+ Schema evolution
+ Untagged data
+ Language support
+ Transparent compression
+ Dynamic typing
+ Native support in MapReduce
+ Rich data structures

[Table of Contents](#Apache-Avro)

## Explain some advantages of Avro.
Pros of Avro are:
+ The Smallest Size.
+ It Compresses block at a time; split table.
+ Maintained Object structure.
+ Also, supports reading old data w/ new schema.

[Table of Contents](#Apache-Avro)

## Explain some disadvantages of Avro.
Cons of Avro are:
+ It must use .NET 4.5, in the case of C# Avro, to make the best use of it.
+ Potentially slower serialization.
+ In order to read/write data, need a schema.

[Table of Contents](#Apache-Avro)

## What do you mean by schema declaration?
In JSON, a Schema is represented by one of:
+ A JSON string
+ A JSON object
+ {“type”: “typename” …attributes…}
+ A JSON array

[Table of Contents](#Apache-Avro)

## Explain the term Serialization?
To transport the data over the network or to store on some persistent storage, the process of translating data structures or objects state into binary or textual form is what we call Serialization. In other words, serialization is also known as as marshaling and deserialization is known as unmarshalling.

[Table of Contents](#Apache-Avro)

## What do you mean by Schema Resolution?
Whether from an RPC or a file, a reader of Avro data, can always parse that data since its schema is offered. Yet it is possible that schema may not be exactly the schema what we expect so for that purpose we use Schema Resolution.

[Table of Contents](#Apache-Avro)

## Explain the Avro Sasl profile?
Basically, SASL offers a framework for authentication and security of network protocols. In Avro also we use SASL Profile for authentication and security purpose.

[Table of Contents](#Apache-Avro)

## What is the way of creating Avro Schemas?
In the format “lightweight text-based data interchange”, JavaScript Object Notation (JSON), the Avro schema gets created.
We can make it in various ways:
+ A JSON string
+ JSON object
+ A JSON array

[Table of Contents](#Apache-Avro)

## Name some Avro Reference Apis?
The classes and methods which we use in the serialization, as well as deserialization of Avro schemas, are:
+ Specific Datum Writer Class
+ Specific Datum Reader Class
+ Data File Writer
+ Data File Reader
+ Class Schema. Parser
+ Interface Generic Record
+ Class Generic Data. Record

[Table of Contents](#Apache-Avro)

## When to use Avro?
Mainly, for two purposes, we use Avro, like:
+ Data serialization
+ RPC (Remote procedure call) protocol
Although, some key points are:
We are able to read the data from disk with applications, by using Avro even which are written in other languages besides java or the JVM.
Also, Avro allows us to transfer data across a remote system without any overhead of java serialization.
We use Avro when we need to store the large set of data on disk, as it conserves space.
Further, by using Avro for RPC, we get a better remote data transfer.

[Table of Contents](#Apache-Avro)

## Explain sort order in brief?
There is a standard sort order for data in Avro which allows data written by one system to be efficiently sorted by another system. As sort order comparisons are sometimes the most frequent per-object operation, it can be an important optimization.

[Table of Contents](#Apache-Avro)

## What is the advantage of Hadoop Over Java Serialization?
As with the help of the Writable objects, Hadoop Writable-based serialization is able to reduce object-creation overhead, which is not possible with the Java native serialization framework that’s why using Hadoop one is an advantage.

[Table of Contents](#Apache-Avro)

## What are the disadvantages of Hadoop Serialization?
The only disadvantage of Hadoop Serialization is that the Writable and Sequence Files have only a Java API. Hence, to solve this issue, Avro comes in picture.

[Table of Contents](#Apache-Avro)