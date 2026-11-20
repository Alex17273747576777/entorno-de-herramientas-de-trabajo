package com.shinku.reader.data.backup
import com.shinku.reader.data.backup.models.*
import kotlinx.serialization.protobuf.ProtoBuf
import okio.Buffer
import java.io.IOException
fun varint(b:Buffer,v:Long) { var x=v; while(x>=128){b.writeByte(((x and 127) or 128).toInt());x=x ushr 7};b.writeByte(x.toInt()) }
fun tag(b:Buffer,f:Long,w:Long)=varint(b,(f shl 3) or w)
fun input(depth:Int):Buffer {val b=Buffer(); repeat(depth){tag(b,900,3)}; repeat(depth){tag(b,900,4)};return b}
fun rejected(b:Buffer){try{BackupStreamDecoder(ProtoBuf).decode(b);error("invalid input accepted")}catch(e:IOException){}}
fun main(){
 val fixture=Backup(backupManga=listOf(BackupManga("test")),backupCategories=listOf(BackupCategory("cat")))
 val encoded=ProtoBuf.encodeToByteArray(Backup.serializer(),fixture);check(BackupStreamDecoder(ProtoBuf).decode(Buffer().write(encoded))==fixture)
 check(BackupStreamDecoder(ProtoBuf).decode(input(64)).backupManga.isEmpty())
 rejected(input(65));rejected(Buffer().also{tag(it,900,3);tag(it,901,4)});rejected(Buffer().also{tag(it,900,3)})
 rejected(Buffer().also{tag(it,1L shl 29,0);varint(it,1)})
 rejected(Buffer().also{tag(it,900,3);tag(it,1L shl 29,0);varint(it,1)})
 rejected(Buffer().also{tag(it,900,4)})
 println("PASS: 8 cases: roundtrip, depth=64, depth=65, mismatch, truncated group, invalid outer and inner fields, stray end")
}
